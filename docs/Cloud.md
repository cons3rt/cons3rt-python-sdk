# Cloud

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_type** | **str** |  | [optional] 
**description** | **str** |  | 
**name** | **str** |  | 
**external_ip_addresses** | **list[str]** |  | [optional] 
**external_ip_source** | **str** |  | 
**features** | [**CloudFeatures**](CloudFeatures.md) |  | [optional] 
**gpu_types** | **list[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**linux_repository_url** | **str** |  | [optional] 
**maximum_impact_level** | **str** |  | 
**networks** | [**list[Network]**](Network.md) |  | [optional] 
**owning_team** | [**Team**](Team.md) |  | 
**provider_feature_configurations** | [**dict(str, AbstractProviderClientConfiguration)**](AbstractProviderClientConfiguration.md) |  | [optional] 
**state** | **str** |  | [optional] 
**template_virtualization_realm** | [**VirtualizationRealm**](VirtualizationRealm.md) |  | [optional] 
**connected_virtualization_realms** | [**list[VirtualizationRealm]**](VirtualizationRealm.md) |  | [optional] 
**virtualization_realms** | [**list[VirtualizationRealm]**](VirtualizationRealm.md) |  | [optional] 
**subtype** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


