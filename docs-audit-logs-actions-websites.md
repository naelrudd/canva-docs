Source: https://www.canva.dev/docs/audit-logs/actions/websites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Websites

## Create a website domain

An `actor` triggers this event when they register a new domain for their website.
For information on Canva websites, visit these Canva Help Center articles:

* [Publish Canva websites](https://www.canva.com/help/publishing-canva-websites/).
* [Change website slug, favicon, and other settings](https://www.canva.com/help/website-settings/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_WEBSITE_DOMAIN`

      **Available values:** The only valid value is `CREATE_WEBSITE_DOMAIN`.
    </Prop.Extras>
  </Prop>

  <Prop name="name" type="string" required mode="output">
    The domain name (subdomain and the top-level domain).
  </Prop>

  <Prop name="domain_type" type="string" mode="output">
    The type of domain being created.

    <Prop.Extras>
      **Available values:**

      * `FREE`: A [free my.canva.site domain name](https://www.canva.com/help/publishing-websites-for-free/) selected by the user or allocated by Canva.
      * `BRING_YOUR_OWN`: An [existing domain name](https://www.canva.com/help/publishing-websites-own-domains/) owned by the user.
      * `PURCHASED`: A domain name [purchased by the user](https://www.canva.com/help/publishing-websites-purchasing-domains/) from Canva.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Update a website domain's details

An `actor` triggers this event when they modify the data associated with an existing domain.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_WEBSITE_DOMAIN`

      **Available values:** The only valid value is `UPDATE_WEBSITE_DOMAIN`.
    </Prop.Extras>
  </Prop>

  <Prop name="update_type" type="string" mode="output">
    <Prop.Extras>
      **Available values:**

      * `RENEW`: Renew a previously purchased domain name registration for an additional period.
      * `REDEEM`: Redeem an expired domain name before it enters the redemption grace period.
      * `RENAME`: Rename a domain to a new public domain, including the website deployed to the current domain.
      * `CONNECT_TO_CANVA`: Connect a domain to Canva for hosting content.
      * `DISCONNECT_FROM_CANVA`: Disconnect a domain from Canva to host content on a different platform.
      * `TRANSFER_DOMAIN`: Unlock a purchased domain and initiate transfer of domain ownership to a different registrar.
      * `CANCEL_TRANSFER`: Cancel an in-progress domain transfer.
      * `UPDATE_DNS_RECORDS`: Update DNS records for the domain.
      * `UPDATE_NAMESERVERS`: Update the nameserver records for the domain.
      * `RESET_NAMESERVERS`: Reset the nameserver records for the domain to their default.
      * `UPDATE_CONTACT`: Update contact information for the domain.
    </Prop.Extras>
  </Prop>

  <Prop name="old_domain_name" type="string" mode="output">
    The old domain name (shown when the `update_type` is `RENAME`)
  </Prop>

  <Prop name="new_domain_name" type="string" mode="output">
    The new domain name (shown when the `update_type` is `RENAME`)
  </Prop>

  <Prop name="old_dns_records" type="DnsRecord[]" mode="output">
    The old DNS records (shown when the `update_type` is either `UPDATE_DNS_RECORDS` or `RESET_NAMESERVERS`).

    <PillAccordion title={<>Properties of <strong>old_dns_records</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="name" type="string" required mode="output">
          The record name.
        </Prop>

        <Prop name="type" type="string" required mode="output">
          The record type.

          <Prop.Extras>
            **Available values:**

            * `A`: IPv4 address record.
            * `AAAA`: IPv6 address record.
            * `CNAME`: Canonical name record.
            * `MX`: Mail exchange record.
            * `TXT`: Text record.
            * `NS`: Nameserver record.
            * `SRV`: Service record.
            * `CAA`: Certificate Authority Authorization record.
          </Prop.Extras>
        </Prop>

        <Prop name="value" type="string" required mode="output">
          The record value.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_dns_records" type="DnsRecord[]" mode="output">
    The new custom DNS records (shown when the `update_type` is either `UPDATE_DNS_RECORDS` or `RESET_NAMESERVERS`).

    <PillAccordion title={<>Properties of <strong>new_dns_records</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="name" type="string" required mode="output">
          The record name.
        </Prop>

        <Prop name="type" type="string" required mode="output">
          The record type.

          <Prop.Extras>
            **Available values:**

            * `A`: IPv4 address record.
            * `AAAA`: IPv6 address record.
            * `CNAME`: Canonical name record.
            * `MX`: Mail exchange record.
            * `TXT`: Text record.
            * `NS`: Nameserver record.
            * `SRV`: Service record.
            * `CAA`: Certificate Authority Authorization record.
          </Prop.Extras>
        </Prop>

        <Prop name="value" type="string" required mode="output">
          The record value.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_contact_info" type="ContactInfo" mode="output">
    The contact information for a domain owner.

    <PillAccordion title={<>Properties of <strong>new_contact_info</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="name" type="string" required mode="output">
          The combined first and last name of the owner.
        </Prop>

        <Prop name="email" type="string" required mode="output">
          The owner's email address.
        </Prop>

        <Prop name="phone" type="string" required mode="output">
          The owner's phone number.
        </Prop>

        <Prop name="address" type="string" required mode="output">
          The street and number of the owner's address.
        </Prop>

        <Prop name="city" type="string" required mode="output">
          The city in the owner's address.
        </Prop>

        <Prop name="country" type="string" required mode="output">
          The two-letter ISO country code representing the country in the owner's address.
        </Prop>

        <Prop name="organization_name" type="string" mode="output">
          The name of the organization that owns the domain.
        </Prop>

        <Prop name="postcode" type="string" mode="output">
          The postal code in the owner's address.
        </Prop>

        <Prop name="state" type="string" mode="output">
          The state of the owner's address.
        </Prop>

        <Prop name="language" type="string" mode="output">
          Language used for messaging the owner.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Delete a website domain

An `actor` triggers this event when they delete a domain.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_WEBSITE_DOMAIN`

      **Available values:** The only valid value is `DELETE_WEBSITE_DOMAIN`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Create an SSO connection for Canva Websites

An `actor` triggers this event when they complete the set up of an SSO connection for Canva Websites.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_WEBSITE_SSO_CONNECTION`

      **Available values:** The only valid value is `CREATE_WEBSITE_SSO_CONNECTION`.
    </Prop.Extras>
  </Prop>

  <Prop name="domains" type="AuditLogWebsiteDomain[]" required mode="output">
    The domains protected by this SSO connection.

    <PillAccordion title={<>Properties of <strong>domains</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The Web Domain ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The domain name.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="name" type="string" mode="output">
    The display name of the SSO connection.
  </Prop>

  <Prop name="idp_issuer" type="string" mode="output">
    The unique identifier of the SAML application, provided by the Identity Provider (IdP).
  </Prop>

  <Prop name="idp_login_url" type="string" mode="output">
    The login URL where users are redirected for authentication.
  </Prop>

  <Prop name="idp_certificate" type="string" mode="output">
    The PEM-encoded X.509 public certificate provided by an Identity Provider (IdP) for SAML authentication.
  </Prop>
</Prop.List>

### Example

## Update an SSO connection for Canva Websites

An `actor` triggers this event when they modify an existing SSO connection for Canva
Websites, including certificate updates.

We only log the team properties that the actor requested changes for.
The changed fields are listed in the `changed_fields` array.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_WEBSITE_SSO_CONNECTION`

      **Available values:** The only valid value is `UPDATE_WEBSITE_SSO_CONNECTION`.
    </Prop.Extras>
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    Fields requested to be changed in this update.

    <Prop.Extras>
      **Available values:**

      * `NAME`: Update the display name of the SSO connection.
      * `DOMAINS`: Update the domains protected by this SSO connection.
      * `IDP_ISSUER`: Update the unique identifier of the SAML application, provided by the Identity Provider (IdP).
      * `IDP_LOGIN_URL`: Update the login URL where users are redirected for authentication.
      * `IDP_CERTIFICATE`: Update the X.509 certificate provided by the Identity Provider (IdP) for SAML authentication.
    </Prop.Extras>
  </Prop>

  <Prop name="old_name" type="string" mode="output">
    The previous name of the SSO connection.
  </Prop>

  <Prop name="new_name" type="string" mode="output">
    The updated name of the SSO connection.
  </Prop>

  <Prop name="old_domains" type="AuditLogWebsiteDomain[]" mode="output">
    The previous domains protected by this SSO connection.

    <PillAccordion title={<>Properties of <strong>old_domains</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The Web Domain ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The domain name.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_domains" type="AuditLogWebsiteDomain[]" mode="output">
    The updated domains protected by this SSO connection.

    <PillAccordion title={<>Properties of <strong>new_domains</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The Web Domain ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The domain name.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="old_idp_issuer" type="string" mode="output">
    The previous Identity Provider (IdP) issuer.
  </Prop>

  <Prop name="new_idp_issuer" type="string" mode="output">
    The updated Identity Provider (IdP) issuer.
  </Prop>

  <Prop name="old_idp_login_url" type="string" mode="output">
    The previous login URL.
  </Prop>

  <Prop name="new_idp_login_url" type="string" mode="output">
    The updated login URL.
  </Prop>

  <Prop name="old_idp_certificate" type="string" mode="output">
    The previous PEM-encoded X.509 public certificate provided by an Identity Provider (IdP) for SAML authentication.
  </Prop>

  <Prop name="new_idp_certificate" type="string" mode="output">
    The updated PEM-encoded X.509 public certificate provided by an Identity Provider (IdP) for SAML authentication.
  </Prop>
</Prop.List>

### Example

## Delete an SSO connection for Canva Websites

An `actor` triggers this event when they delete an SSO connection for Canva Websites.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_WEBSITE_SSO_CONNECTION`

      **Available values:** The only valid value is `DELETE_WEBSITE_SSO_CONNECTION`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

