import yaml

str = """general:
  description: Cisco IOS XRv Router platform
  nature: router
  read_only: true
schema_version: "0.0.1"
configuration:
  generator:
    driver: iosxrv
  provisioning:
    volume_name: cidata
    media_type: iso
    files:
    - name: "iosxr_config.txt"
      content: ''
      editable: true
    - name: "iosxr_config_admin.txt"
      # TODO: is this the correct name / path?
      # Configuration Manager could not find any admin configuration
      # to apply from '/disk0:/config/admin/admin.cfg'.
      content: |
        !! IOS XR Admin Configuration
        username cisco
          group root-system
          secret 0 cisco
        !
        end
      editable: false"""

print(var := (yaml.load(str, Loader=yaml.FullLoader)))
print(var["configuration"]["provisioning"]["files"][0]["content"])
print(len(var["configuration"]["provisioning"]["files"]))