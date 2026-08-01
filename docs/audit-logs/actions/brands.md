Source: https://www.canva.dev/docs/audit-logs/actions/brands.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/audit-logs/llms.txt
> Use this file to discover all available pages before exploring further.

# Brands

## Create a Brand Kit

An `actor` triggers this event when they create a new Brand Kit.
For details, see [Canva Help: Setting up Brand Kits](https://www.canva.com/help/brand-kit/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `CREATE_BRAND_KIT`

      **Available values:** The only valid value is `CREATE_BRAND_KIT`.
    </Prop.Extras>
  </Prop>

  <Prop name="name" type="string" mode="output">
    The name of the Brand Kit.
  </Prop>
</Prop.List>

### Example

## Update a Brand Kit's details

An `actor` triggers this event when they update a Brand Kit.
For details, see [Canva Help: Setting up Brand Kits](https://www.canva.com/help/brand-kit/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `UPDATE_BRAND_KIT`

      **Available values:** The only valid value is `UPDATE_BRAND_KIT`.
    </Prop.Extras>
  </Prop>

  <Prop name="changed_fields" type="string[]" mode="output">
    The fields the `actor` requested changes for in this update.

    <Prop.Extras>
      **Available values:**

      * `NAME`: The name of the Brand Kit.
      * `SHARES`: The shares of the Brand Kit.
      * `FONTS`: The fonts of the Brand Kit.
      * `FOLDER_LINKS`: The links to the Brand Kit folders.
      * `INGREDIENT`: The ingredient of the Brand Kit.
      * `ICON`: The icon of the Brand Kit.
      * `GUIDELINES`: The guidelines design of the Brand Kit.
    </Prop.Extras>
  </Prop>

  <Prop name="old_name" type="string" mode="output">
    The previous name of the Brand Kit.
  </Prop>

  <Prop name="new_name" type="string" mode="output">
    The new name of the Brand Kit.
  </Prop>

  <Prop name="old_shares" type="BrandKitShare[]" mode="output">
    The shares of the Brand Kit.

    <Tabs>
      <Tab name="TEAM">
        A team the Brand Kit is shared with.

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

      <Tab name="FOLDER">
        A folder the Brand Kit is shared with.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `FOLDER`

              **Available values:** The only valid value is `FOLDER`.
            </Prop.Extras>
          </Prop>

          <Prop name="folder" type="AuditLogFolder" required mode="output">
            A Canva folder.

            <PillAccordion title={<>Properties of <strong>folder</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The folder ID.
                </Prop>

                <Prop name="name" type="string" mode="output">
                  The name of the folder.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="ORGANIZATION">
        An organization the Brand Kit is shared with.

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

      <Tab name="USER">
        A user the Brand Kit is shared with (within a team).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `USER`

              **Available values:** The only valid value is `USER`.
            </Prop.Extras>
          </Prop>

          <Prop name="user" type="AuditLogUser" required mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>user</strong></>}>
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

      <Tab name="GROUP">
        A group the Brand Kit is shared with (within a team).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GROUP`

              **Available values:** The only valid value is `GROUP`.
            </Prop.Extras>
          </Prop>

          <Prop name="group" type="AuditLogGroup" required mode="output">
            A Canva group.

            <PillAccordion title={<>Properties of <strong>group</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The group ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the group.
                </Prop>
              </Prop.List>
            </PillAccordion>
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
    </Tabs>
  </Prop>

  <Prop name="new_shares" type="BrandKitShare[]" mode="output">
    The shares of the Brand Kit.

    <Tabs>
      <Tab name="TEAM">
        A team the Brand Kit is shared with.

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

      <Tab name="FOLDER">
        A folder the Brand Kit is shared with.

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `FOLDER`

              **Available values:** The only valid value is `FOLDER`.
            </Prop.Extras>
          </Prop>

          <Prop name="folder" type="AuditLogFolder" required mode="output">
            A Canva folder.

            <PillAccordion title={<>Properties of <strong>folder</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The folder ID.
                </Prop>

                <Prop name="name" type="string" mode="output">
                  The name of the folder.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="ORGANIZATION">
        An organization the Brand Kit is shared with.

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

      <Tab name="USER">
        A user the Brand Kit is shared with (within a team).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `USER`

              **Available values:** The only valid value is `USER`.
            </Prop.Extras>
          </Prop>

          <Prop name="user" type="AuditLogUser" required mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>user</strong></>}>
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

      <Tab name="GROUP">
        A group the Brand Kit is shared with (within a team).

        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GROUP`

              **Available values:** The only valid value is `GROUP`.
            </Prop.Extras>
          </Prop>

          <Prop name="group" type="AuditLogGroup" required mode="output">
            A Canva group.

            <PillAccordion title={<>Properties of <strong>group</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The group ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the group.
                </Prop>
              </Prop.List>
            </PillAccordion>
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
    </Tabs>
  </Prop>

  <Prop name="old_fonts" type="BrandKitFont[]" mode="output">
    The fonts of the Brand Kit.

    <PillAccordion title={<>Properties of <strong>old_fonts</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The ID of the font family.
        </Prop>

        <Prop name="font_family" type="string" mode="output">
          The name of the font family.
        </Prop>

        <Prop name="font_style" type="string" mode="output">
          The style of the font.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_fonts" type="BrandKitFont[]" mode="output">
    The fonts of the Brand Kit.

    <PillAccordion title={<>Properties of <strong>new_fonts</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The ID of the font family.
        </Prop>

        <Prop name="font_family" type="string" mode="output">
          The name of the font family.
        </Prop>

        <Prop name="font_style" type="string" mode="output">
          The style of the font.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="old_folder_links" type="BrandKitFolderLink[]" mode="output">
    The previous folder links to the Brand Kit.

    <PillAccordion title={<>Properties of <strong>old_folder_links</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="folder" type="AuditLogFolder" required mode="output">
          A Canva folder.

          <PillAccordion title={<>Properties of <strong>folder</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                The folder ID.
              </Prop>

              <Prop name="name" type="string" mode="output">
                The name of the folder.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="type" type="string" mode="output">
          The type of the brand assets in the folder.

          <Prop.Extras>
            **Available values:**

            * `CHARTS`: A folder with Charts.
            * `GRAPHICS`: A folder with Graphics.
            * `ICONS`: A folder with Icons.
            * `LOGOS`: A folder with Logos.
            * `PHOTOS`: A folder with Photos.
          </Prop.Extras>
        </Prop>

        <Prop name="ingredient" type="BrandKitLinkedIngredient" mode="output">
          A linked ingredient of the Brand Kit.

          <PillAccordion title={<>Properties of <strong>ingredient</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                ID of the ingredient.
              </Prop>

              <Prop name="name" type="string" mode="output">
                The name of the ingredient.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_folder_links" type="BrandKitFolderLink[]" mode="output">
    The new folder links to the Brand Kit.

    <PillAccordion title={<>Properties of <strong>new_folder_links</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="folder" type="AuditLogFolder" required mode="output">
          A Canva folder.

          <PillAccordion title={<>Properties of <strong>folder</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                The folder ID.
              </Prop>

              <Prop name="name" type="string" mode="output">
                The name of the folder.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="type" type="string" mode="output">
          The type of the brand assets in the folder.

          <Prop.Extras>
            **Available values:**

            * `CHARTS`: A folder with Charts.
            * `GRAPHICS`: A folder with Graphics.
            * `ICONS`: A folder with Icons.
            * `LOGOS`: A folder with Logos.
            * `PHOTOS`: A folder with Photos.
          </Prop.Extras>
        </Prop>

        <Prop name="ingredient" type="BrandKitLinkedIngredient" mode="output">
          A linked ingredient of the Brand Kit.

          <PillAccordion title={<>Properties of <strong>ingredient</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                ID of the ingredient.
              </Prop>

              <Prop name="name" type="string" mode="output">
                The name of the ingredient.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="old_ingredient" type="BrandKitIngredient" mode="output">
    An ingredient of the Brand Kit.

    <PillAccordion title={<>Properties of <strong>old_ingredient</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="name" type="string" mode="output">
          A name of the ingredient.
        </Prop>

        <Prop name="id" type="string" mode="output">
          ID of the ingredient.
        </Prop>

        <Prop name="guidelines" type="string" mode="output">
          User-provided guidelines to help members of the team understand how, where, and when to use the ingredient.
        </Prop>

        <Prop name="color_palettes" type="BrandKitColorPalette[]" mode="output">
          The color palettes of the Brand Kit.

          <PillAccordion title={<>Properties of <strong>color_palettes</strong></>}>
            <Prop.List>
              <Prop name="name" type="string" mode="output">
                The name of the color palette.
              </Prop>

              <Prop name="colors" type="BrandKitColor[]" mode="output">
                The colors in the palette.

                <PillAccordion title={<>Properties of <strong>colors</strong></>}>
                  <Prop.List>
                    <Prop name="name" type="string" mode="output">
                      The name of the color.
                    </Prop>

                    <Prop name="hex" type="string" mode="output">
                      The hex value of the color.
                    </Prop>

                    <Prop name="cmyk" type="string" mode="output">
                      The CMYK value of the color.
                    </Prop>

                    <Prop name="gradient" type="BrandKitGradient" mode="output">
                      A color gradient in the Brand Kit.

                      <Tabs>
                        <Tab name="LINEAR">
                          A linear gradient in the Brand Kit.

                          <Prop.List>
                            <Prop name="type" type="string" required mode="output">
                              <Prop.Extras>
                                **Default value:** `LINEAR`

                                **Available values:** The only valid value is `LINEAR`.
                              </Prop.Extras>
                            </Prop>

                            <Prop name="stops" type="BrandKitGradientStop[]" required mode="output">
                              The color stops in the gradient.

                              <PillAccordion title={<>Properties of <strong>stops</strong></>}>
                                <Prop.List>
                                  <Prop name="color" type="string" required mode="output">
                                    The color of the stop.
                                  </Prop>

                                  <Prop name="transparency" type="number" required mode="output">
                                    The transparency of the stop.
                                  </Prop>

                                  <Prop name="position" type="number" required mode="output">
                                    The position of the stop as a percentage along the gradient line.
                                  </Prop>
                                </Prop.List>
                              </PillAccordion>
                            </Prop>

                            <Prop name="rotation" type="number" required mode="output">
                              The rotation of the gradient in degrees.
                            </Prop>
                          </Prop.List>
                        </Tab>

                        <Tab name="RADIAL">
                          A radial gradient in the Brand Kit.

                          <Prop.List>
                            <Prop name="type" type="string" required mode="output">
                              <Prop.Extras>
                                **Default value:** `RADIAL`

                                **Available values:** The only valid value is `RADIAL`.
                              </Prop.Extras>
                            </Prop>

                            <Prop name="stops" type="BrandKitGradientStop[]" required mode="output">
                              The color stops in the gradient.

                              <PillAccordion title={<>Properties of <strong>stops</strong></>}>
                                <Prop.List>
                                  <Prop name="color" type="string" required mode="output">
                                    The color of the stop.
                                  </Prop>

                                  <Prop name="transparency" type="number" required mode="output">
                                    The transparency of the stop.
                                  </Prop>

                                  <Prop name="position" type="number" required mode="output">
                                    The position of the stop as a percentage along the gradient line.
                                  </Prop>
                                </Prop.List>
                              </PillAccordion>
                            </Prop>

                            <Prop name="center" type="object" required mode="output">
                              The center of the radial gradient. If the `top` and `left` are both zero, the center
                              is in the top-left of the gradient.

                              <PillAccordion title={<>Properties of <strong>center</strong></>}>
                                <Prop.List>
                                  <Prop name="top" type="number" required mode="output">
                                    The top position of the center, as a percentage down from the top of the gradient.
                                  </Prop>

                                  <Prop name="left" type="number" required mode="output">
                                    The left position of the center, as a percentage from the left of the gradient.
                                  </Prop>
                                </Prop.List>
                              </PillAccordion>
                            </Prop>
                          </Prop.List>
                        </Tab>
                      </Tabs>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="text_styles" type="BrandKitTextStylesGroup[]" mode="output">
          The text styles of the Brand Kit.

          <PillAccordion title={<>Properties of <strong>text_styles</strong></>}>
            <Prop.List>
              <Prop name="name" type="string" required mode="output">
                The name of the text style group.
              </Prop>

              <Prop name="text_styles" type="BrandKitTextStyle[]" required mode="output">
                The formatting set for the text style.

                <PillAccordion title={<>Properties of <strong>text_styles</strong></>}>
                  <Prop.List>
                    <Prop name="font" type="BrandKitFont" required mode="output">
                      A font in the Brand Kit.

                      <PillAccordion title={<>Properties of <strong>font</strong></>}>
                        <Prop.List>
                          <Prop name="id" type="string" required mode="output">
                            The ID of the font family.
                          </Prop>

                          <Prop name="font_family" type="string" mode="output">
                            The name of the font family.
                          </Prop>

                          <Prop name="font_style" type="string" mode="output">
                            The style of the font.
                          </Prop>
                        </Prop.List>
                      </PillAccordion>
                    </Prop>

                    <Prop name="size" type="integer" required mode="output">
                      The size of the text style in pixels.
                    </Prop>

                    <Prop name="name" type="string" mode="output">
                      The name of the text style.
                    </Prop>

                    <Prop name="custom_name" type="string" mode="output">
                      The user-defined text style name.
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="voice" type="string" mode="output">
          The voice of the brand.
        </Prop>

        <Prop name="assets" type="BrandKitAsset[]" mode="output">
          The assets in the ingredient.

          <PillAccordion title={<>Properties of <strong>assets</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                An ID of the asset.
              </Prop>

              <Prop name="name" type="string" mode="output">
                A name of the asset.
              </Prop>

              <Prop name="file_name" type="string" mode="output">
                A name of the asset file.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="dos_and_donts" type="BrandKitDosAndDonts" mode="output">
          The dos and donts for the ingredient

          <PillAccordion title={<>Properties of <strong>dos_and_donts</strong></>}>
            <Prop.List>
              <Prop name="dos" type="string[]" mode="output">
                The dos of the ingredient.
              </Prop>

              <Prop name="donts" type="string[]" mode="output">
                The donts of the ingredient.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_ingredient" type="BrandKitIngredient" mode="output">
    An ingredient of the Brand Kit.

    <PillAccordion title={<>Properties of <strong>new_ingredient</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="name" type="string" mode="output">
          A name of the ingredient.
        </Prop>

        <Prop name="id" type="string" mode="output">
          ID of the ingredient.
        </Prop>

        <Prop name="guidelines" type="string" mode="output">
          User-provided guidelines to help members of the team understand how, where, and when to use the ingredient.
        </Prop>

        <Prop name="color_palettes" type="BrandKitColorPalette[]" mode="output">
          The color palettes of the Brand Kit.

          <PillAccordion title={<>Properties of <strong>color_palettes</strong></>}>
            <Prop.List>
              <Prop name="name" type="string" mode="output">
                The name of the color palette.
              </Prop>

              <Prop name="colors" type="BrandKitColor[]" mode="output">
                The colors in the palette.

                <PillAccordion title={<>Properties of <strong>colors</strong></>}>
                  <Prop.List>
                    <Prop name="name" type="string" mode="output">
                      The name of the color.
                    </Prop>

                    <Prop name="hex" type="string" mode="output">
                      The hex value of the color.
                    </Prop>

                    <Prop name="cmyk" type="string" mode="output">
                      The CMYK value of the color.
                    </Prop>

                    <Prop name="gradient" type="BrandKitGradient" mode="output">
                      A color gradient in the Brand Kit.

                      <Tabs>
                        <Tab name="LINEAR">
                          A linear gradient in the Brand Kit.

                          <Prop.List>
                            <Prop name="type" type="string" required mode="output">
                              <Prop.Extras>
                                **Default value:** `LINEAR`

                                **Available values:** The only valid value is `LINEAR`.
                              </Prop.Extras>
                            </Prop>

                            <Prop name="stops" type="BrandKitGradientStop[]" required mode="output">
                              The color stops in the gradient.

                              <PillAccordion title={<>Properties of <strong>stops</strong></>}>
                                <Prop.List>
                                  <Prop name="color" type="string" required mode="output">
                                    The color of the stop.
                                  </Prop>

                                  <Prop name="transparency" type="number" required mode="output">
                                    The transparency of the stop.
                                  </Prop>

                                  <Prop name="position" type="number" required mode="output">
                                    The position of the stop as a percentage along the gradient line.
                                  </Prop>
                                </Prop.List>
                              </PillAccordion>
                            </Prop>

                            <Prop name="rotation" type="number" required mode="output">
                              The rotation of the gradient in degrees.
                            </Prop>
                          </Prop.List>
                        </Tab>

                        <Tab name="RADIAL">
                          A radial gradient in the Brand Kit.

                          <Prop.List>
                            <Prop name="type" type="string" required mode="output">
                              <Prop.Extras>
                                **Default value:** `RADIAL`

                                **Available values:** The only valid value is `RADIAL`.
                              </Prop.Extras>
                            </Prop>

                            <Prop name="stops" type="BrandKitGradientStop[]" required mode="output">
                              The color stops in the gradient.

                              <PillAccordion title={<>Properties of <strong>stops</strong></>}>
                                <Prop.List>
                                  <Prop name="color" type="string" required mode="output">
                                    The color of the stop.
                                  </Prop>

                                  <Prop name="transparency" type="number" required mode="output">
                                    The transparency of the stop.
                                  </Prop>

                                  <Prop name="position" type="number" required mode="output">
                                    The position of the stop as a percentage along the gradient line.
                                  </Prop>
                                </Prop.List>
                              </PillAccordion>
                            </Prop>

                            <Prop name="center" type="object" required mode="output">
                              The center of the radial gradient. If the `top` and `left` are both zero, the center
                              is in the top-left of the gradient.

                              <PillAccordion title={<>Properties of <strong>center</strong></>}>
                                <Prop.List>
                                  <Prop name="top" type="number" required mode="output">
                                    The top position of the center, as a percentage down from the top of the gradient.
                                  </Prop>

                                  <Prop name="left" type="number" required mode="output">
                                    The left position of the center, as a percentage from the left of the gradient.
                                  </Prop>
                                </Prop.List>
                              </PillAccordion>
                            </Prop>
                          </Prop.List>
                        </Tab>
                      </Tabs>
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="text_styles" type="BrandKitTextStylesGroup[]" mode="output">
          The text styles of the Brand Kit.

          <PillAccordion title={<>Properties of <strong>text_styles</strong></>}>
            <Prop.List>
              <Prop name="name" type="string" required mode="output">
                The name of the text style group.
              </Prop>

              <Prop name="text_styles" type="BrandKitTextStyle[]" required mode="output">
                The formatting set for the text style.

                <PillAccordion title={<>Properties of <strong>text_styles</strong></>}>
                  <Prop.List>
                    <Prop name="font" type="BrandKitFont" required mode="output">
                      A font in the Brand Kit.

                      <PillAccordion title={<>Properties of <strong>font</strong></>}>
                        <Prop.List>
                          <Prop name="id" type="string" required mode="output">
                            The ID of the font family.
                          </Prop>

                          <Prop name="font_family" type="string" mode="output">
                            The name of the font family.
                          </Prop>

                          <Prop name="font_style" type="string" mode="output">
                            The style of the font.
                          </Prop>
                        </Prop.List>
                      </PillAccordion>
                    </Prop>

                    <Prop name="size" type="integer" required mode="output">
                      The size of the text style in pixels.
                    </Prop>

                    <Prop name="name" type="string" mode="output">
                      The name of the text style.
                    </Prop>

                    <Prop name="custom_name" type="string" mode="output">
                      The user-defined text style name.
                    </Prop>
                  </Prop.List>
                </PillAccordion>
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="voice" type="string" mode="output">
          The voice of the brand.
        </Prop>

        <Prop name="assets" type="BrandKitAsset[]" mode="output">
          The assets in the ingredient.

          <PillAccordion title={<>Properties of <strong>assets</strong></>}>
            <Prop.List>
              <Prop name="id" type="string" required mode="output">
                An ID of the asset.
              </Prop>

              <Prop name="name" type="string" mode="output">
                A name of the asset.
              </Prop>

              <Prop name="file_name" type="string" mode="output">
                A name of the asset file.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>

        <Prop name="dos_and_donts" type="BrandKitDosAndDonts" mode="output">
          The dos and donts for the ingredient

          <PillAccordion title={<>Properties of <strong>dos_and_donts</strong></>}>
            <Prop.List>
              <Prop name="dos" type="string[]" mode="output">
                The dos of the ingredient.
              </Prop>

              <Prop name="donts" type="string[]" mode="output">
                The donts of the ingredient.
              </Prop>
            </Prop.List>
          </PillAccordion>
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="old_icon" type="AuditLogImage" mode="output">
    A Canva image.

    <PillAccordion title={<>Properties of <strong>old_icon</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The image ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the image.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_icon" type="AuditLogImage" mode="output">
    A Canva image.

    <PillAccordion title={<>Properties of <strong>new_icon</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The image ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the image.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="old_guidelines" type="AuditLogDesign" mode="output">
    A Canva design.

    <PillAccordion title={<>Properties of <strong>old_guidelines</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The design ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the design.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>

  <Prop name="new_guidelines" type="AuditLogDesign" mode="output">
    A Canva design.

    <PillAccordion title={<>Properties of <strong>new_guidelines</strong></>} defaultExpanded={true}>
      <Prop.List>
        <Prop name="id" type="string" required mode="output">
          The design ID.
        </Prop>

        <Prop name="name" type="string" mode="output">
          The name of the design.
        </Prop>
      </Prop.List>
    </PillAccordion>
  </Prop>
</Prop.List>

### Example

## Delete a Brand Kit

An `actor` triggers this event when they delete a Brand Kit.
For details, see [Canva Help: Setting up Brand Kits](https://www.canva.com/help/brand-kit/).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `DELETE_BRAND_KIT`

      **Available values:** The only valid value is `DELETE_BRAND_KIT`.
    </Prop.Extras>
  </Prop>
</Prop.List>

### Example

## Send a brand template share notification

An `actor` triggers this event when they share a brand template.
Canva will attempt to send an email and an in-app notification to the user the brand template is shared with (`recipient`).

<Prop.List>
  <Prop name="type" type="string" required mode="output">
    <Prop.Extras>
      **Default value:** `SEND_BRAND_TEMPLATE_SHARE_NOTIFICATION`

      **Available values:** The only valid value is `SEND_BRAND_TEMPLATE_SHARE_NOTIFICATION`.
    </Prop.Extras>
  </Prop>

  <Prop name="recipient" type="ShareNotificationRecipient" required mode="output">
    The recipient of the share notification.

    The recipient can be a user, a group, an organization, or an email address.

    <Tabs>
      <Tab name="USER_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `USER_RECIPIENT`

              **Available values:** The only valid value is `USER_RECIPIENT`.
            </Prop.Extras>
          </Prop>

          <Prop name="user" type="AuditLogUser" required mode="output">
            A Canva user.

            <PillAccordion title={<>Properties of <strong>user</strong></>}>
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

      <Tab name="GROUP_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `GROUP_RECIPIENT`

              **Available values:** The only valid value is `GROUP_RECIPIENT`.
            </Prop.Extras>
          </Prop>

          <Prop name="group" type="AuditLogGroup" required mode="output">
            A Canva group.

            <PillAccordion title={<>Properties of <strong>group</strong></>}>
              <Prop.List>
                <Prop name="id" type="string" required mode="output">
                  The group ID.
                </Prop>

                <Prop name="display_name" type="string" mode="output">
                  The display name of the group.
                </Prop>
              </Prop.List>
            </PillAccordion>
          </Prop>
        </Prop.List>
      </Tab>

      <Tab name="ORGANIZATION_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `ORGANIZATION_RECIPIENT`

              **Available values:** The only valid value is `ORGANIZATION_RECIPIENT`.
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

      <Tab name="EMAIL_RECIPIENT">
        <Prop.List>
          <Prop name="type" type="string" required mode="output">
            <Prop.Extras>
              **Default value:** `EMAIL_RECIPIENT`

              **Available values:** The only valid value is `EMAIL_RECIPIENT`.
            </Prop.Extras>
          </Prop>

          <Prop name="email" type="string" required mode="output">
            The email address the design invite was sent to.
          </Prop>
        </Prop.List>
      </Tab>
    </Tabs>
  </Prop>

  <Prop name="message" type="string" mode="output">
    An optional message from the `actor` to the `recipient`.
  </Prop>
</Prop.List>

### Example

