Search_Bar = (
    "/html/body/mainapp/div[1]/div[2]/div[1]/div[1]/input",
    "#root > div.jioMainGrid > div.jioGridRight > div.jioGridRightTop > div.jioSearchBar > input"
)
# Login Page
Login_Username = (
    "//input[@name='username']",
    "input[placeholder=''][name='username']",
    ""
)

Login_Password = (
    "//input[@name='password']",
    "input[placeholder=''][name='password']",
    ""
)
Login_LoginBtn = (
    "//button[normalize-space()='LOGIN']",
    "button[type='submit']",
    "")

DefaultLogin_AdminPass = (
    "//input[@name='adminPassword']",
    "input[placeholder=''][name='adminPassword']",
    ""
)
DefaultLogin_CnfAdminPass = (
    "//input[@name='confirmAdminPassword']",
    "input[placeholder=''][name='confirmAdminPassword']",
    ""
)
DefaultLogin_GuestPass = (
    "//input[@name='guestPassword']",
    "input[placeholder=''][name='guestPassword']",
    ""
)
DefaultLogin_CnfGuestPass = ("//input[@name='confirmGuestPassword']",
                             "input[placeholder=''][name='confirmGuestPassword']",
                             ""
                             )

DefaultLogin_UpdateBtn = (
    "//button[normalize-space()='Update']",
    "button[type='submit']",
    ""
)

# Device Information

WanInfo_MacAddress = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]",
    "div div div:nth-child(2) form:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(3) div:nth-child(1) div:nth-child(2)"
    ""
)
WanInfo_IPv6 = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[2]/form[1]/div[1]/div[1]/div[3]/div[3]/div[2]",
    "div div div:nth-child(2) form:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(3) div:nth-child(3) div:nth-child(2)",
    ""
)

# Device Status
SysInfo_FirmwareVersion = (
    '/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]',
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
)
SysInfo_SerialNumber = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[3]/div[5]/div[2]/div[1]",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1)"
)
SysInfo_ModelName = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(7) > div:nth-child(2)"
)

# Lan Iformation

LANInfo_MACAddress = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]",
    "body mainapp div div div div div:nth-child(2) div:nth-child(1) div:nth-child(3) div:nth-child(3) div:nth-child(2)"
)
LANInfo_IPv4Address = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]",
    "body mainapp div div div div div:nth-child(2) div:nth-child(1) div:nth-child(3) div:nth-child(3) div:nth-child(2)"
)
LANInfo_IPv6Address = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[3]/div[5]/div[2]",
    "body mainapp div div div div div:nth-child(2) div:nth-child(1) div:nth-child(3) div:nth-child(3) div:nth-child(2)"
)

LANInfo_IPv4DHCPServer = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[3]/div[7]/div[2]/div[1]",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(7) > div:nth-child(2) > div:nth-child(1)"
)

# Wireless
Wireless_Ssid = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div/form/div/div[1]/div[3]/div[9]/input",
    "#\/Wireless > div.jioWrtSectionContentContainer > div.jioWrtSectionContent > div:nth-child(9) > input[type=text]"
)

Wireless_ChangePasswordToggle_1 = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div/form/div/div[1]/div[3]/div[15]/div/label/span",
    ""
)

Wireless_ChangePasswordToggle_2 = (
    '/html/body/mainapp/div[1]/div[2]/div[4]/div/form/div/div[1]/div[3]/div[15]/label[2]/span',
    ""
)

Wireless_Password = (
    '/html/body/mainapp/div[1]/div[2]/div[4]/div/form/div/div[1]/div[3]/div[17]/input',
    ""
)

Wireless_Confirmpassword = (
    '/html/body/mainapp/div[1]/div[2]/div[4]/div/form/div/div[1]/div[3]/div[19]/input',
    ""
)

Wireless_SaveButton = (
    '/html/body/mainapp/div[1]/div[2]/div[4]/div/form/div/div[3]/button',
    ""
)

# maintainence >> Reset/Reboot
FactoryDefaultsReboot_DropDown = (
    "//span[normalize-space()='Select Option']",
    "div[data-name='selectDefaultsReboot_jioSelectLabelContainer'] span[class='jioDropdown']",
    ""
)

FactoryDefaultsReboot_FactoryDefaultopt = (
    "//li[normalize-space()='Restore to Factory Defaults']",
    "li[data-enable='-1'][data-value='2']"
)

FactoryDefaultsReboot_FactoryDefaultBtn = (
    "//button[normalize-space()='DEFAULTS']",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > form:nth-child(4) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)"
)

FactoryDefaultsReboot_FactoryDefaultCnfBtn = (
    "//div[@class='jioWrtModalWindowContainer jioFactoyDefaultRebootModal']//button[@type='button'][normalize-space()='RESTORE']",
    "div[class='jioWrtModalWindowContainer jioFactoyDefaultRebootModal'] button[type='button']"
)

FactoryDefaultsReboot_RebootOpt = (
    "//li[normalize-space()='Reboot']",
    "li[data-enable='-1'][data-value='3']"
)

FactoryDefaultsReboot_RebootBtn = (
    "//button[normalize-space()='Reboot']",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > form:nth-child(4) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)"
)

FactoryDefaultsReboot_RebootCnfBtn = (
    "//div[@class='jioModalWindowFooter']//button[@type='button'][normalize-space()='Reboot']",
    "div[class='jioWrtModalWindowContainer jioFactoyDefaultRebootModal'] button[type='button']"
)

# maintainence >> BackUp
BackupSettings_BackupIcon = (
    "//div[@class='iconActionDownload']//*[name()='svg']//*[name()='path' and @id='icon']",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > svg:nth-child(1) > path:nth-child(3)"
)

# maintainence >> Restor
RestoreSettings_RestoreOpt = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[2]/form[1]/div/div[1]/div[2]/div[1]/input",
    "#selectTheSavedSettings"
)
RestoreSettings_RestoreBtn = (
    "//div[@class='jioWrtSectionBottom']//button[@type='button'][normalize-space()='RESTORE']",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)",
)

RestoreSettings_RestoreCnfBtn = (
    "//div[@class='jioModalWindowFooter']//button[@type='button'][normalize-space()='RESTORE']",
    'div[class="jioWrtModalWindowContainer jioRestoreModal1708683448635bc6721d4-2887-0ce5-ea9b-a4b4646f3422"] button[type="button"]')

# Firmware Upgrade
FirmwareUpgrade_ImgFile = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/form/div/div[1]/div[2]/div[1]/input",
    "#selectTheNewFirmware"
)
FirmwareUpgrade_SignFile = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/form/div/div[1]/div[2]/div[3]/input",
    "#selectTheNewSignature"
)
FirmwareUpgrade_UpgradeBtn = (
    "//button[normalize-space()='UPGRADE']",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)",
)
FirmwareUpgrade_UpgradeCnfBtn = (
    '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/form/div[3]/button',
    "form[class='jioWrtPromptWindow jioWrtUpdateWindow'] button[type='button']"
)

PingTraceroute4_DomainName = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/form[1]/div/div[1]/div[3]/div[1]/input",
    'input[placeholder=""][name="ipv4AddressDomainName"]'
)
PingTraceroute4_Type = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/form[1]/div[1]/div[1]/div[3]/div[3]/div[1]/span[1]",
    "div[data-name='traceroutePing_jioSelectLabelContainer'] span[class='jioDropdown']"
)

PingTraceroute4_StartBtn = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/form[1]/div/div[3]/button",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)"
)

PingTraceroute4_Msg = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/div[1]/form/div[2]/div/div/code",
    "#root > div.jioMainGrid > div.jioGridRight > div.jioGridRightMain > div:nth-child(1) > div.jioWrtModalWindowContainer.jioPingModal1709718241604f8baa250-2c87-fdf1-0b92-93b01b4f6da8 > form > div.jioModalWindowContentContainer > div > div > code")
PingTraceroute4_Msg_CancleBtn = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > svg:nth-child(1) > path:nth-child(2)")

PingTraceroute6_DomainName = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/form[2]/div/div[1]/div[3]/div[1]/input",
    'input[placeholder=""][name="ipv6AddressDomainName"]'
)
PingTraceroute6_Type = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/form[2]/div[1]/div[1]/div[3]/div[3]/div[1]/span[1]",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > span:nth-child(1)"
)

PingTraceroute6_StartBtn = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/form[2]/div/div[3]/button",
    "#\/Diagnostics\/Ping6 > div.jioWrtSectionBottom > button"

)
PingTraceroute6_Msg = (
    "/html/body/mainapp/div[1]/div[2]/div[4]/div[1]/div[2]/form/div[2]/div/div/code",
    "#root > div.jioMainGrid > div.jioGridRight > div.jioGridRightMain > div:nth-child(1) > div.jioWrtModalWindowContainer.jioPing6Modal170971120538788a9d69a-82e8-6565-5f52-cdb2268adf6a > form > div.jioModalWindowContentContainer > div > div > code"
)
PingTraceroute6_Msg_CancleBtn = (
    "/html[1]/body[1]/mainapp[1]/div[1]/div[2]/div[4]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='path'][1]",
    "body > mainapp:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(4) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > svg:nth-child(1) > path:nth-child(2)"
)
