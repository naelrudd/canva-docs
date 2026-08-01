Source: https://www.canva.dev/docs/audit-logs/actions/users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Users

## Create a user

An `actor` triggers this event when they create (or provision) a new Canva user, including
when an individual creates a Canva user account by visiting a team invitation link.

The `reason` field contains the reason the user was created. For example, they accepted a
team invitation or they were provisioned by a SCIM provider.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_USER`

      **Available values:** The only valid value is `CREATE_USER`.
    </Prop.Extras>
  </Prop>

  <Prop name="display_name" type="string" mode="output">
    The user's display name. This is used to represent the user with text in a UI.
  </Prop>

  <Prop name="first_name" type="string" mode="output">
    The user's first name.
  </Prop>

  <Prop name="last_name" type="string" mode="output">
    The user's last name.
  </Prop>

  <Prop name="email" type="string" mode="output">
    The user's email address.
  </Prop>

  <Prop name="email_verified" type="boolean" mode="output">
    Whether the user's email address has been verified.
  </Prop>

  <Prop name="phone_number" type="string" mode="output">
    The user's phone number.
  </Prop>

  <Prop name="country_code" type="string" mode="output">
    The user's country code, shown on user's public profile page.
  </Prop>

  <Prop name="locale" type="string" mode="output">
    The supported locale for the user.
  </Prop>

  <Prop name="managing_entity" type="ManagingEntity" mode="output">
    The entity that manages the user.

    <Tabs>
      <Tab name="TEAM">
        A managing entity that is a team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `TEAM`

              **Available values:** The only valid value is `TEAM`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The team ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the team.

                  For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="ORGANIZATION">
        A managing entity that is an organization.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `ORGANIZATION`

              **Available values:** The only valid value is `ORGANIZATION`.
            </Prop.Extras>
          </Prop>

          <Prop name="organization" type="AuditLogOrganization" required mode="output">
            A Canva organization.

            <PillAccordion title={<>Properties of <strong>organization</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The organization ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the organization.

                  For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>

  <Prop name="saml_accounts" type="SamlAccount[]" mode="output">
    SAML accounts for the user.

    <PillAccordion title={<>Properties of <strong>saml_accounts</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="idp_issuer" type="string" required mode="output">
          A unique identifier for the SAML identity provider.
        </Prop>

        <Prop name="name_id" type="string" required mode="output">
          The unique identifier for the user, within the scope of `idp_issuer`. This value is often an email address.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="oauth_accounts" type="OauthAccount[]" mode="output">
    OAuth accounts for the user.

    <PillAccordion title={<>Properties of <strong>oauth_accounts</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="platform" type="string" required mode="output">
          The OAuth platform.
        </Prop>

        <Prop name="external_user_id" type="string" required mode="output">
          The account ID for the user on the external platform.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="totp_mfa_enabled" type="boolean" mode="output">
    Whether TOTP MFA (Time-based One-Time Password Multi-Factor Authentication) is enabled for the user.
  </Prop>

  <Prop name="sms_mfa_enabled" type="boolean" mode="output">
    Whether SMS MFA (SMS-based Multi-Factor Authentication) is enabled for the user.
  </Prop>

  <Prop name="reason" type="TeamMembershipChangeReason" mode="output">
    The reason for the change.

    <Tabs>
      <Tab name="INVITATION_ACCEPTED">
        An invitation to join team was accepted

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `INVITATION_ACCEPTED`

              **Available values:** The only valid value is `INVITATION_ACCEPTED`.
            </Prop.Extras>
          </Prop>

          <Prop name="inviter" type="AuditLogUser" mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>inviter</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The user ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the user.

                  For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.
                </Prop>

                <Prop name="email" type="string" mode="output">
                  The email address of the user.

                  For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="JOIN_POLICY_ALLOWED">
        The change was permitted by your [Team discovery and settings](https://www.canva.com/help/team-discovery/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `JOIN_POLICY_ALLOWED`

              **Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="REQUEST_TO_JOIN_APPROVED">
        A user request to join your team was approved.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `REQUEST_TO_JOIN_APPROVED`

              **Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SCIM">
        The change was made through your team's configured [SCIM Identity Provider](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SCIM`

              **Available values:** The only valid value is `SCIM`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="SAML_JIT_PROVISIONING">
        SAML Just-In-Time provisioning. This event can be triggered by events like a user
        [linking their Canva account with your SSO provider](https://www.canva.com/help/sso-linking/)
        or when you [set up Single Sign-On (SSO)](https://www.canva.com/help/set-up-sso/) for your
        team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `SAML_JIT_PROVISIONING`

              **Available values:** The only valid value is `SAML_JIT_PROVISIONING`.
            </Prop.Extras>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="PROVISIONING_POLICY">
        This change was triggered by an provisioning policy.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `PROVISIONING_POLICY`

              **Available values:** The only valid value is `PROVISIONING_POLICY`.
            </Prop.Extras>
          </Prop>

          <Prop name="provisioning_policy" type="AuditLogProvisioningPolicy" mode="output">
            A Canva provisioning policy.

            <PillAccordion title={<>Properties of <strong>provisioning_policy</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The provisioning policy ID.
                </Prop>

                <Prop name="name" type="string" mode="output">
                  The provisioning policy name.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

### Example

## Update a user's details

An `actor` triggers this event when they update a user's account details.
This includes when a user updates their own account details.

We only log the user properties that the actor requested changes for.
The changed fields are listed in the `changed_fields` array.

Some changed fields, such as `PASSWORD`, might be in the `changed_fields` array but won't have a property
included in the log.

If the user was updated as part of the login process, the actor might be set to `ANONYMOUS`.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_USER`

      **Available values:** The only valid value is `UPDATE_USER`.
    </Prop.Extras>
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    Fields requested to be changed in this update.

    <Prop.Extras>
      **Available values:**

      * `PASSWORD`: The user's password.
      * `DISPLAY_NAME`: The user's display name.
      * `FIRST_NAME`: The user's first name.
      * `LAST_NAME`: The user's last name.
      * `EMAIL`: The user's email address.
      * `EMAIL_VERIFIED`: Whether the user's email address has been verified.
      * `PHONE_NUMBER`: The user's phone number.
      * `CITY`: The user's city.
      * `COUNTRY_CODE`: The user's country code.
      * `LOCALE`: The user's locale.
      * `MANAGING_ENTITY`: The entity that manages the user.
      * `SAML_ACCOUNTS`: SAML accounts.
      * `OAUTH_ACCOUNTS`: OAUTH accounts.
      * `TOTP_MFA_ENABLED`: Whether TOTP MFA (Time-based One-Time Password Multi-Factor Authentication) is enabled for the user.
      * `SMS_MFA_ENABLED`: Whether SMS MFA (SMS-based Multi-Factor Authentication) is enabled for the user.
      * `PASSKEYS`: The user's passkeys.
    </Prop.Extras>
  </Prop>

  <Prop name="display_name" type="string" mode="output">
    The user's display name. This is used to represent the user with text in a UI.
  </Prop>

  <Prop name="first_name" type="string" mode="output">
    The user's first name.
  </Prop>

  <Prop name="last_name" type="string" mode="output">
    The user's last name.
  </Prop>

  <Prop name="email" type="string" mode="output">
    The user's email address.
  </Prop>

  <Prop name="email_verified" type="boolean" mode="output">
    Whether the user's email address has been verified.
  </Prop>

  <Prop name="phone_number" type="string" mode="output">
    The user's phone number.
  </Prop>

  <Prop name="country_code" type="string" mode="output">
    The user's country code, shown on user's public profile page.
  </Prop>

  <Prop name="locale" type="string" mode="output">
    The supported locale for the user.
  </Prop>

  <Prop name="managing_entity" type="ManagingEntity" mode="output">
    The entity that manages the user.

    <Tabs>
      <Tab name="TEAM">
        A managing entity that is a team.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `TEAM`

              **Available values:** The only valid value is `TEAM`.
            </Prop.Extras>
          </Prop>

          <Prop name="team" type="AuditLogTeam" required mode="output">
            A Canva team.

            <PillAccordion title={<>Properties of <strong>team</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The team ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the team.

                  For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="ORGANIZATION">
        A managing entity that is an organization.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `ORGANIZATION`

              **Available values:** The only valid value is `ORGANIZATION`.
            </Prop.Extras>
          </Prop>

          <Prop name="organization" type="AuditLogOrganization" required mode="output">
            A Canva organization.

            <PillAccordion title={<>Properties of <strong>organization</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The organization ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the organization.

                  For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>

  <Prop name="saml_accounts" type="SamlAccount[]" mode="output">
    SAML accounts for the user.

    <PillAccordion title={<>Properties of <strong>saml_accounts</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="idp_issuer" type="string" required mode="output">
          A unique identifier for the SAML identity provider.
        </Prop>

        <Prop name="name_id" type="string" required mode="output">
          The unique identifier for the user, within the scope of `idp_issuer`. This value is often an email address.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="oauth_accounts" type="OauthAccount[]" mode="output">
    OAuth accounts for the user.

    <PillAccordion title={<>Properties of <strong>oauth_accounts</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="platform" type="string" required mode="output">
          The OAuth platform.
        </Prop>

        <Prop name="external_user_id" type="string" required mode="output">
          The account ID for the user on the external platform.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="totp_mfa_enabled" type="boolean" mode="output">
    Whether TOTP MFA (Time-based One-Time Password Multi-Factor Authentication) is enabled for the user.
  </Prop>

  <Prop name="sms_mfa_enabled" type="boolean" mode="output">
    Whether SMS MFA (SMS-based Multi-Factor Authentication) is enabled for the user.
  </Prop>

  <Prop name="passkeys" type="Passkey[]" mode="output">
    Passkeys for the user.

    <PillAccordion title={<>Properties of <strong>passkeys</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The passkey ID.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="reason" type="UpdateUserChangeReason" mode="output">
    Why the user's details changed.

    <Tabs>
      <Tab name="PASSWORD_RESET_WITH_LINK">
        The user's password was reset and their identity was verified using a link in an email.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `PASSWORD_RESET_WITH_LINK`

              **Available values:** The only valid value is `PASSWORD_RESET_WITH_LINK`.
            </Prop.Extras>
          </Prop>

          <Prop name="email" type="string" mode="output">
            The email address used for verification when resetting the password.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="PASSWORD_RESET_WITH_SMS_CODE">
        The user's password was reset and their identity was verified using a code the user received via SMS.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `PASSWORD_RESET_WITH_SMS_CODE`

              **Available values:** The only valid value is `PASSWORD_RESET_WITH_SMS_CODE`.
            </Prop.Extras>
          </Prop>

          <Prop name="phone_number" type="string" mode="output">
            The phone number used for verification when resetting the password.
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="PASSWORD_RESET_WITH_EMAIL_CODE">
        The user's password was reset and their identity was verified using an email code.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `PASSWORD_RESET_WITH_EMAIL_CODE`

              **Available values:** The only valid value is `PASSWORD_RESET_WITH_EMAIL_CODE`.
            </Prop.Extras>
          </Prop>

          <Prop name="email" type="string" mode="output">
            The email address used for verification when resetting the password.
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>
</Prop.List>

### Example

## Delete a user

An `actor` triggers this event when they delete a user's account.
This includes when a user deletes their own account.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_USER`

      **Available values:** The only valid value is `DELETE_USER`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Cancel the deletion of a user

An `actor` triggers this event when they cancel or undo the deletion of a user's account.
This includes when a user cancels the deletion of their own account.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UNDELETE_USER`

      **Available values:** The only valid value is `UNDELETE_USER`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Create multi-factor authentication (MFA) backup codes

An `actor` triggers this event when they generate multi-factor authentication (MFA) backup codes for their account.
For details on generating MFA backup codes, see [Canva Help: Setting up Multi-Factor Authentication (MFA) —
Generate backup codes](https://www.canva.com/help/login-verification/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_MFA_BACKUP_CODES`

      **Available values:** The only valid value is `CREATE_MFA_BACKUP_CODES`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Log in

An `actor` triggers this event when they log into Canva.

The actor will be `USER` if the login is successful. If the login is unsuccessful, the actor will be `ANONYMOUS`.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `LOGIN`

      **Available values:** The only valid value is `LOGIN`.
    </Prop.Extras>
  </Prop>

  <Prop name="login_type" type="string" mode="output">
    The general type of user login being attempted.

    <Prop.Extras>
      **Available values:**

      * `PASSWORD`: User login with credentials, such as email address, user ID, phone number, and password.
      * `ONE_TIME_PASSWORD`: User login with a temporary code delivered to the user's email address or phone.
      * `MULTI_FACTOR_AUTHENTICATION`: User login with multi-factor authentication.
      * `OAUTH`: User login with a social account or other third-party provider.
      * `SAML`: User login with single sign-on for a specific email domain.
      * `PASSKEY`: User login with a passkey (such as a security key).
      * `OTHER`: Other types of user login.
      * `LEARNING_TOOLS_INTEROPERABILITY`: User login for education users from a Learning Management System.
    </Prop.Extras>
  </Prop>

  <Prop name="oauth_platform" type="string" mode="output">
    The OAuth platform used for login. Only set if the `login_type` is `OAUTH`.

    <Prop.Extras>
      **Available values:**

      * `APPLE`
      * `ATLASSIAN`
      * `CLEVER`
      * `DROPBOX`
      * `FACEBOOK`
      * `GITHUB`
      * `GOOGLE`
      * `HUAWEI`
      * `INSTAGRAM`
      * `KAKAO`
      * `LARK`
      * `LINE`
      * `LINKEDIN`
      * `MAILCHIMP`
      * `MICROSOFT`
      * `NAVER`
      * `PINTEREST`
      * `QQ`
      * `SLACK`
      * `TRELLO`
      * `TUMBLR`
      * `TURKEY_EDU`
      * `TWITTER`
      * `WECHAT`
      * `WEIBO`
      * `YAHOO_JAPAN`
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Log out

An `actor` triggers this event when they log out of Canva.

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `LOGOUT`

      **Available values:** The only valid value is `LOGOUT`.
    </Prop.Extras>
  </Prop>

  <Prop name="all_users" type="boolean" mode="output">
    Whether the `actor` has requested that all users on the device are logged out. If `false`, only the current user is logged out.
  </Prop>

  <Prop name="all_sessions" type="boolean" mode="output">
    Whether the `actor` has requested that all sessions across all devices are logged out. If `false`, only the current session is logged out.
  </Prop>
</Prop.List>

### Example

