-- ÒsánVault canonical persistence foundation
-- M5 staging-only migration. Do NOT run against production until certification.

BEGIN;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE SCHEMA IF NOT EXISTS osanvault;

CREATE TABLE IF NOT EXISTS osanvault.organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'archived')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    external_subject TEXT,
    display_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'archived')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (organization_id, external_subject)
);

CREATE TABLE IF NOT EXISTS osanvault.assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    legacy_id TEXT,
    name TEXT NOT NULL,
    asset_type TEXT NOT NULL DEFAULT 'property',
    location_text TEXT,
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'pending', 'verified', 'active', 'suspended', 'archived')),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    asset_id UUID REFERENCES osanvault.assets(id),
    document_type TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 1 CHECK (version > 0),
    content_hash TEXT,
    storage_reference TEXT,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'verified', 'rejected', 'archived')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.verification_cases (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    asset_id UUID REFERENCES osanvault.assets(id),
    subject_user_id UUID REFERENCES osanvault.users(id),
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'in_review', 'approved', 'rejected', 'cancelled')),
    decision TEXT,
    decided_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.offerings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    asset_id UUID REFERENCES osanvault.assets(id),
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'review', 'approved', 'active', 'closed', 'cancelled')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.investments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    offering_id UUID NOT NULL REFERENCES osanvault.offerings(id),
    investor_user_id UUID REFERENCES osanvault.users(id),
    quantity NUMERIC(38, 18) NOT NULL CHECK (quantity >= 0),
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'settled')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.treasury_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    currency_code TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'frozen', 'closed')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.ledger_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    treasury_account_id UUID NOT NULL REFERENCES osanvault.treasury_accounts(id),
    entry_reference TEXT NOT NULL,
    direction TEXT NOT NULL CHECK (direction IN ('debit', 'credit')),
    amount NUMERIC(38, 18) NOT NULL CHECK (amount > 0),
    currency_code TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_id UUID,
    idempotency_key TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.tokenization_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    asset_id UUID NOT NULL REFERENCES osanvault.assets(id),
    token_symbol TEXT NOT NULL,
    network TEXT,
    contract_address TEXT,
    onchain_reference TEXT,
    status TEXT NOT NULL DEFAULT 'proposed' CHECK (status IN ('proposed', 'approved', 'deployed', 'suspended', 'retired')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS osanvault.audit_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES osanvault.organizations(id),
    actor_user_id UUID REFERENCES osanvault.users(id),
    action TEXT NOT NULL,
    resource_type TEXT NOT NULL,
    resource_id UUID,
    event_hash TEXT,
    previous_event_hash TEXT,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_assets_org ON osanvault.assets(organization_id);
CREATE INDEX IF NOT EXISTS idx_documents_asset ON osanvault.documents(asset_id);
CREATE INDEX IF NOT EXISTS idx_verification_asset ON osanvault.verification_cases(asset_id);
CREATE INDEX IF NOT EXISTS idx_investments_offering ON osanvault.investments(offering_id);
CREATE INDEX IF NOT EXISTS idx_ledger_account ON osanvault.ledger_entries(treasury_account_id);
CREATE INDEX IF NOT EXISTS idx_audit_resource ON osanvault.audit_events(resource_type, resource_id);

COMMIT;
