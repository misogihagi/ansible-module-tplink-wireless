# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: utility/model.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 6, 30, 0, "", "utility/model.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13utility/model.proto\x12\x06router"\x08\n\x06Status"\x0c\n\nQuickSetup"8\n\rOperationMode\x12\'\n\x04mode\x18\x01 \x01(\x0e\x32\x19.router.OperationModeType"\xbd\x01\n\x07Network\x12 \n\x03wan\x18\x01 \x01(\x0b\x32\x13.router.Network.WAN\x12 \n\x03lan\x18\x02 \x01(\x0b\x32\x13.router.Network.LAN\x12+\n\tmac_clone\x18\x03 \x01(\x0b\x32\x18.router.Network.MACClone\x1a\x05\n\x03WAN\x1a.\n\x03LAN\x12\x12\n\nip_address\x18\x01 \x01(\t\x12\x13\n\x0bsubnet_mask\x18\x02 \x01(\t\x1a\n\n\x08MACClone"\xea\x07\n\rWireless24GHz\x12;\n\x0e\x62\x61sic_settings\x18\x01 \x01(\x0b\x32#.router.Wireless24GHz.BasicSettings\x12&\n\x03wps\x18\x02 \x01(\x0b\x32\x19.router.Wireless24GHz.WPS\x12\x30\n\x08security\x18\x03 \x01(\x0b\x32\x1e.router.Wireless24GHz.Security\x12\x39\n\rmac_filtering\x18\x04 \x01(\x0b\x32".router.Wireless24GHz.MACFiltering\x12\x41\n\x11\x61\x64vanced_settings\x18\x05 \x01(\x0b\x32&.router.Wireless24GHz.AdvancedSettings\x12\x34\n\nstatistics\x18\x06 \x01(\x0b\x32 .router.Wireless24GHz.Statistics\x1a\xc8\x04\n\rBasicSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x04mode\x18\x02 \x01(\x0e\x32(.router.Wireless24GHz.BasicSettings.Mode\x12<\n\x07\x63hannel\x18\x03 \x01(\x0e\x32+.router.Wireless24GHz.BasicSettings.Channel\x12O\n\x11\x63hannel_bandwidth\x18\x04 \x01(\x0e\x32\x34.router.Wireless24GHz.BasicSettings.ChannelBandwidth\x12\x18\n\x10\x65nable_broadcast\x18\x05 \x01(\x08"#\n\x04Mode\x12\n\n\x06N_ONLY\x10\x00\x12\x06\n\x02GN\x10\x01\x12\x07\n\x03\x42GN\x10\x02"\xe2\x01\n\x07\x43hannel\x12\x10\n\x0c\x43HANNEL_AUTO\x10\x00\x12\r\n\tCHANNEL_1\x10\x01\x12\r\n\tCHANNEL_2\x10\x02\x12\r\n\tCHANNEL_3\x10\x03\x12\r\n\tCHANNEL_4\x10\x04\x12\r\n\tCHANNEL_5\x10\x05\x12\r\n\tCHANNEL_6\x10\x06\x12\r\n\tCHANNEL_7\x10\x07\x12\r\n\tCHANNEL_8\x10\x08\x12\r\n\tCHANNEL_9\x10\t\x12\x0e\n\nCHANNEL_10\x10\n\x12\x0e\n\nCHANNEL_11\x10\x0b\x12\x0e\n\nCHANNEL_12\x10\x0c\x12\x0e\n\nCHANNEL_13\x10\r">\n\x10\x43hannelBandwidth\x12\x12\n\x0e\x42\x41NDWIDTH_AUTO\x10\x00\x12\n\n\x06MHz_20\x10\x01\x12\n\n\x06MHz_40\x10\x02\x1a\x05\n\x03WPS\x1a\n\n\x08Security\x1a\x0e\n\x0cMACFiltering\x1a\x12\n\x10\x41\x64vancedSettings\x1a\x0c\n\nStatistics"\x0e\n\x0cGuestNetwork"\xcb\x01\n\x04\x44HCP\x12\'\n\x08settings\x18\x01 \x01(\x0b\x32\x15.router.DHCP.Settings\x12,\n\x0b\x63lient_list\x18\x02 \x01(\x0b\x32\x17.router.DHCP.ClientList\x12<\n\x13\x61\x64\x64ress_reservation\x18\x03 \x01(\x0b\x32\x1f.router.DHCP.AddressReservation\x1a\n\n\x08Settings\x1a\x0c\n\nClientList\x1a\x14\n\x12\x41\x64\x64ressReservation"\xf7\x01\n\nForwarding\x12\x38\n\x0evirtual_server\x18\x01 \x01(\x0b\x32 .router.Forwarding.VirtualServer\x12\x34\n\x0cport_trigger\x18\x02 \x01(\x0b\x32\x1e.router.Forwarding.PortTrigger\x12#\n\x03\x64mz\x18\x03 \x01(\x0b\x32\x16.router.Forwarding.DMZ\x12%\n\x04upnp\x18\x04 \x01(\x0b\x32\x17.router.Forwarding.UPnP\x1a\x0f\n\rVirtualServer\x1a\r\n\x0bPortTrigger\x1a\x05\n\x03\x44MZ\x1a\x06\n\x04UPnP"\xc6\x02\n\x08Security\x12\x36\n\x0e\x62\x61sic_security\x18\x01 \x01(\x0b\x32\x1e.router.Security.BasicSecurity\x12<\n\x11\x61\x64vanced_security\x18\x02 \x01(\x0b\x32!.router.Security.AdvancedSecurity\x12:\n\x10local_management\x18\x03 \x01(\x0b\x32 .router.Security.LocalManagement\x12<\n\x11remote_management\x18\x04 \x01(\x0b\x32!.router.Security.RemoteManagement\x1a\x0f\n\rBasicSecurity\x1a\x12\n\x10\x41\x64vancedSecurity\x1a\x11\n\x0fLocalManagement\x1a\x12\n\x10RemoteManagement"\x11\n\x0fParentalControl"\xec\x01\n\rAccessControl\x12*\n\x05rules\x18\x01 \x01(\x0b\x32\x1b.router.AccessControl.Rules\x12(\n\x04host\x18\x02 \x01(\x0b\x32\x1a.router.AccessControl.Host\x12,\n\x06target\x18\x03 \x01(\x0b\x32\x1c.router.AccessControl.Target\x12\x30\n\x08schedule\x18\x04 \x01(\x0b\x32\x1e.router.AccessControl.Schedule\x1a\x07\n\x05Rules\x1a\x06\n\x04Host\x1a\x08\n\x06Target\x1a\n\n\x08Schedule"\xc2\x01\n\x0f\x41\x64vancedRouting\x12\x42\n\x11static_route_list\x18\x01 \x01(\x0b\x32\'.router.AdvancedRouting.StaticRouteList\x12\x44\n\x12system_route_table\x18\x02 \x01(\x0b\x32(.router.AdvancedRouting.SystemRouteTable\x1a\x11\n\x0fStaticRouteList\x1a\x12\n\x10SystemRouteTable"\x12\n\x10\x42\x61ndwidthControl"\x9c\x01\n\x0cIPMACBinding\x12>\n\x10\x62inding_settings\x18\x01 \x01(\x0b\x32$.router.IPMACBinding.BindingSettings\x12.\n\x08\x61rp_list\x18\x02 \x01(\x0b\x32\x1c.router.IPMACBinding.ARPList\x1a\x11\n\x0f\x42indingSettings\x1a\t\n\x07\x41RPList"\x0c\n\nDynamicDNS"\x81\x01\n\x04IPv6\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.router.IPv6.Status\x12\x1d\n\x03wan\x18\x02 \x01(\x0b\x32\x10.router.IPv6.WAN\x12\x1d\n\x03lan\x18\x03 \x01(\x0b\x32\x10.router.IPv6.LAN\x1a\x08\n\x06Status\x1a\x05\n\x03WAN\x1a\x05\n\x03LAN"\x88\x05\n\x0bSystemTools\x12\x37\n\rtime_settings\x18\x01 \x01(\x0b\x32 .router.SystemTools.TimeSettings\x12\x34\n\x0b\x64iagnostics\x18\x02 \x01(\x0b\x32\x1f.router.SystemTools.Diagnostics\x12=\n\x10\x66irmware_upgrade\x18\x03 \x01(\x0b\x32#.router.SystemTools.FirmwareUpgrade\x12\x37\n\rfactory_reset\x18\x04 \x01(\x0b\x32 .router.SystemTools.FactoryReset\x12\x39\n\x0e\x62\x61\x63kup_restore\x18\x05 \x01(\x0b\x32!.router.SystemTools.BackupRestore\x12*\n\x06reboot\x18\x06 \x01(\x0b\x32\x1a.router.SystemTools.Reboot\x12.\n\x08password\x18\x07 \x01(\x0b\x32\x1c.router.SystemTools.Password\x12\x31\n\nsystem_log\x18\x08 \x01(\x0b\x32\x1d.router.SystemTools.SystemLog\x12\x32\n\nstatistics\x18\t \x01(\x0b\x32\x1e.router.SystemTools.Statistics\x1a\x0e\n\x0cTimeSettings\x1a\r\n\x0b\x44iagnostics\x1a\x11\n\x0f\x46irmwareUpgrade\x1a\x0e\n\x0c\x46\x61\x63toryReset\x1a\x0f\n\rBackupRestore\x1a\x08\n\x06Reboot\x1a\x1c\n\x08Password\x12\x10\n\x08username\x18\x01 \x01(\t\x1a\x0b\n\tSystemLog\x1a\x0c\n\nStatistics"\x08\n\x06Logout"\xf5\x05\n\x0cRouterConfig\x12\x1e\n\x06status\x18\x01 \x01(\x0b\x32\x0e.router.Status\x12\'\n\x0bquick_setup\x18\x02 \x01(\x0b\x32\x12.router.QuickSetup\x12-\n\x0eoperation_mode\x18\x03 \x01(\x0b\x32\x15.router.OperationMode\x12 \n\x07network\x18\x04 \x01(\x0b\x32\x0f.router.Network\x12.\n\x0fwireless_2_4ghz\x18\x05 \x01(\x0b\x32\x15.router.Wireless24GHz\x12+\n\rguest_network\x18\x06 \x01(\x0b\x32\x14.router.GuestNetwork\x12\x1a\n\x04\x64hcp\x18\x07 \x01(\x0b\x32\x0c.router.DHCP\x12&\n\nforwarding\x18\x08 \x01(\x0b\x32\x12.router.Forwarding\x12"\n\x08security\x18\t \x01(\x0b\x32\x10.router.Security\x12\x31\n\x10parental_control\x18\n \x01(\x0b\x32\x17.router.ParentalControl\x12-\n\x0e\x61\x63\x63\x65ss_control\x18\x0b \x01(\x0b\x32\x15.router.AccessControl\x12\x31\n\x10\x61\x64vanced_routing\x18\x0c \x01(\x0b\x32\x17.router.AdvancedRouting\x12\x33\n\x11\x62\x61ndwidth_control\x18\r \x01(\x0b\x32\x18.router.BandwidthControl\x12,\n\x0eip_mac_binding\x18\x0e \x01(\x0b\x32\x14.router.IPMACBinding\x12\'\n\x0b\x64ynamic_dns\x18\x0f \x01(\x0b\x32\x12.router.DynamicDNS\x12\x1a\n\x04ipv6\x18\x10 \x01(\x0b\x32\x0c.router.IPv6\x12)\n\x0csystem_tools\x18\x11 \x01(\x0b\x32\x13.router.SystemTools\x12\x1e\n\x06logout\x18\x12 \x01(\x0b\x32\x0e.router.Logout*Q\n\x11OperationModeType\x12\x13\n\x0fWIRELESS_ROUTER\x10\x00\x12\x08\n\x04WISP\x10\x01\x12\x0f\n\x0b\x42RIDGE_MODE\x10\x02\x12\x0c\n\x08REPEATER\x10\x03\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "utility.model_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_OPERATIONMODETYPE"]._serialized_start = 4312
    _globals["_OPERATIONMODETYPE"]._serialized_end = 4393
    _globals["_STATUS"]._serialized_start = 31
    _globals["_STATUS"]._serialized_end = 39
    _globals["_QUICKSETUP"]._serialized_start = 41
    _globals["_QUICKSETUP"]._serialized_end = 53
    _globals["_OPERATIONMODE"]._serialized_start = 55
    _globals["_OPERATIONMODE"]._serialized_end = 111
    _globals["_NETWORK"]._serialized_start = 114
    _globals["_NETWORK"]._serialized_end = 303
    _globals["_NETWORK_WAN"]._serialized_start = 238
    _globals["_NETWORK_WAN"]._serialized_end = 243
    _globals["_NETWORK_LAN"]._serialized_start = 245
    _globals["_NETWORK_LAN"]._serialized_end = 291
    _globals["_NETWORK_MACCLONE"]._serialized_start = 293
    _globals["_NETWORK_MACCLONE"]._serialized_end = 303
    _globals["_WIRELESS24GHZ"]._serialized_start = 306
    _globals["_WIRELESS24GHZ"]._serialized_end = 1308
    _globals["_WIRELESS24GHZ_BASICSETTINGS"]._serialized_start = 655
    _globals["_WIRELESS24GHZ_BASICSETTINGS"]._serialized_end = 1239
    _globals["_WIRELESS24GHZ_BASICSETTINGS_MODE"]._serialized_start = 911
    _globals["_WIRELESS24GHZ_BASICSETTINGS_MODE"]._serialized_end = 946
    _globals["_WIRELESS24GHZ_BASICSETTINGS_CHANNEL"]._serialized_start = 949
    _globals["_WIRELESS24GHZ_BASICSETTINGS_CHANNEL"]._serialized_end = 1175
    _globals["_WIRELESS24GHZ_BASICSETTINGS_CHANNELBANDWIDTH"]._serialized_start = 1177
    _globals["_WIRELESS24GHZ_BASICSETTINGS_CHANNELBANDWIDTH"]._serialized_end = 1239
    _globals["_WIRELESS24GHZ_WPS"]._serialized_start = 1241
    _globals["_WIRELESS24GHZ_WPS"]._serialized_end = 1246
    _globals["_WIRELESS24GHZ_SECURITY"]._serialized_start = 1248
    _globals["_WIRELESS24GHZ_SECURITY"]._serialized_end = 1258
    _globals["_WIRELESS24GHZ_MACFILTERING"]._serialized_start = 1260
    _globals["_WIRELESS24GHZ_MACFILTERING"]._serialized_end = 1274
    _globals["_WIRELESS24GHZ_ADVANCEDSETTINGS"]._serialized_start = 1276
    _globals["_WIRELESS24GHZ_ADVANCEDSETTINGS"]._serialized_end = 1294
    _globals["_WIRELESS24GHZ_STATISTICS"]._serialized_start = 1296
    _globals["_WIRELESS24GHZ_STATISTICS"]._serialized_end = 1308
    _globals["_GUESTNETWORK"]._serialized_start = 1310
    _globals["_GUESTNETWORK"]._serialized_end = 1324
    _globals["_DHCP"]._serialized_start = 1327
    _globals["_DHCP"]._serialized_end = 1530
    _globals["_DHCP_SETTINGS"]._serialized_start = 1484
    _globals["_DHCP_SETTINGS"]._serialized_end = 1494
    _globals["_DHCP_CLIENTLIST"]._serialized_start = 1496
    _globals["_DHCP_CLIENTLIST"]._serialized_end = 1508
    _globals["_DHCP_ADDRESSRESERVATION"]._serialized_start = 1510
    _globals["_DHCP_ADDRESSRESERVATION"]._serialized_end = 1530
    _globals["_FORWARDING"]._serialized_start = 1533
    _globals["_FORWARDING"]._serialized_end = 1780
    _globals["_FORWARDING_VIRTUALSERVER"]._serialized_start = 1735
    _globals["_FORWARDING_VIRTUALSERVER"]._serialized_end = 1750
    _globals["_FORWARDING_PORTTRIGGER"]._serialized_start = 1752
    _globals["_FORWARDING_PORTTRIGGER"]._serialized_end = 1765
    _globals["_FORWARDING_DMZ"]._serialized_start = 1767
    _globals["_FORWARDING_DMZ"]._serialized_end = 1772
    _globals["_FORWARDING_UPNP"]._serialized_start = 1774
    _globals["_FORWARDING_UPNP"]._serialized_end = 1780
    _globals["_SECURITY"]._serialized_start = 1783
    _globals["_SECURITY"]._serialized_end = 2109
    _globals["_SECURITY_BASICSECURITY"]._serialized_start = 2035
    _globals["_SECURITY_BASICSECURITY"]._serialized_end = 2050
    _globals["_SECURITY_ADVANCEDSECURITY"]._serialized_start = 2052
    _globals["_SECURITY_ADVANCEDSECURITY"]._serialized_end = 2070
    _globals["_SECURITY_LOCALMANAGEMENT"]._serialized_start = 2072
    _globals["_SECURITY_LOCALMANAGEMENT"]._serialized_end = 2089
    _globals["_SECURITY_REMOTEMANAGEMENT"]._serialized_start = 2091
    _globals["_SECURITY_REMOTEMANAGEMENT"]._serialized_end = 2109
    _globals["_PARENTALCONTROL"]._serialized_start = 2111
    _globals["_PARENTALCONTROL"]._serialized_end = 2128
    _globals["_ACCESSCONTROL"]._serialized_start = 2131
    _globals["_ACCESSCONTROL"]._serialized_end = 2367
    _globals["_ACCESSCONTROL_RULES"]._serialized_start = 2330
    _globals["_ACCESSCONTROL_RULES"]._serialized_end = 2337
    _globals["_ACCESSCONTROL_HOST"]._serialized_start = 2339
    _globals["_ACCESSCONTROL_HOST"]._serialized_end = 2345
    _globals["_ACCESSCONTROL_TARGET"]._serialized_start = 2347
    _globals["_ACCESSCONTROL_TARGET"]._serialized_end = 2355
    _globals["_ACCESSCONTROL_SCHEDULE"]._serialized_start = 2357
    _globals["_ACCESSCONTROL_SCHEDULE"]._serialized_end = 2367
    _globals["_ADVANCEDROUTING"]._serialized_start = 2370
    _globals["_ADVANCEDROUTING"]._serialized_end = 2564
    _globals["_ADVANCEDROUTING_STATICROUTELIST"]._serialized_start = 2527
    _globals["_ADVANCEDROUTING_STATICROUTELIST"]._serialized_end = 2544
    _globals["_ADVANCEDROUTING_SYSTEMROUTETABLE"]._serialized_start = 2546
    _globals["_ADVANCEDROUTING_SYSTEMROUTETABLE"]._serialized_end = 2564
    _globals["_BANDWIDTHCONTROL"]._serialized_start = 2566
    _globals["_BANDWIDTHCONTROL"]._serialized_end = 2584
    _globals["_IPMACBINDING"]._serialized_start = 2587
    _globals["_IPMACBINDING"]._serialized_end = 2743
    _globals["_IPMACBINDING_BINDINGSETTINGS"]._serialized_start = 2715
    _globals["_IPMACBINDING_BINDINGSETTINGS"]._serialized_end = 2732
    _globals["_IPMACBINDING_ARPLIST"]._serialized_start = 2734
    _globals["_IPMACBINDING_ARPLIST"]._serialized_end = 2743
    _globals["_DYNAMICDNS"]._serialized_start = 2745
    _globals["_DYNAMICDNS"]._serialized_end = 2757
    _globals["_IPV6"]._serialized_start = 2760
    _globals["_IPV6"]._serialized_end = 2889
    _globals["_IPV6_STATUS"]._serialized_start = 31
    _globals["_IPV6_STATUS"]._serialized_end = 39
    _globals["_IPV6_WAN"]._serialized_start = 238
    _globals["_IPV6_WAN"]._serialized_end = 243
    _globals["_IPV6_LAN"]._serialized_start = 245
    _globals["_IPV6_LAN"]._serialized_end = 250
    _globals["_SYSTEMTOOLS"]._serialized_start = 2892
    _globals["_SYSTEMTOOLS"]._serialized_end = 3540
    _globals["_SYSTEMTOOLS_TIMESETTINGS"]._serialized_start = 3392
    _globals["_SYSTEMTOOLS_TIMESETTINGS"]._serialized_end = 3406
    _globals["_SYSTEMTOOLS_DIAGNOSTICS"]._serialized_start = 3408
    _globals["_SYSTEMTOOLS_DIAGNOSTICS"]._serialized_end = 3421
    _globals["_SYSTEMTOOLS_FIRMWAREUPGRADE"]._serialized_start = 3423
    _globals["_SYSTEMTOOLS_FIRMWAREUPGRADE"]._serialized_end = 3440
    _globals["_SYSTEMTOOLS_FACTORYRESET"]._serialized_start = 3442
    _globals["_SYSTEMTOOLS_FACTORYRESET"]._serialized_end = 3456
    _globals["_SYSTEMTOOLS_BACKUPRESTORE"]._serialized_start = 3458
    _globals["_SYSTEMTOOLS_BACKUPRESTORE"]._serialized_end = 3473
    _globals["_SYSTEMTOOLS_REBOOT"]._serialized_start = 3475
    _globals["_SYSTEMTOOLS_REBOOT"]._serialized_end = 3483
    _globals["_SYSTEMTOOLS_PASSWORD"]._serialized_start = 3485
    _globals["_SYSTEMTOOLS_PASSWORD"]._serialized_end = 3513
    _globals["_SYSTEMTOOLS_SYSTEMLOG"]._serialized_start = 3515
    _globals["_SYSTEMTOOLS_SYSTEMLOG"]._serialized_end = 3526
    _globals["_SYSTEMTOOLS_STATISTICS"]._serialized_start = 1296
    _globals["_SYSTEMTOOLS_STATISTICS"]._serialized_end = 1308
    _globals["_LOGOUT"]._serialized_start = 3542
    _globals["_LOGOUT"]._serialized_end = 3550
    _globals["_ROUTERCONFIG"]._serialized_start = 3553
    _globals["_ROUTERCONFIG"]._serialized_end = 4310
# @@protoc_insertion_point(module_scope)
