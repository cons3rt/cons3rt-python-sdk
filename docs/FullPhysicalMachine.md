# FullPhysicalMachine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**offline** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**creator** | [**MinimalUser**](MinimalUser.md) |  | [optional] 
**owning_project** | [**MinimalProject**](MinimalProject.md) |  | [optional] 
**trusted_projects** | [**list[MinimalProject]**](MinimalProject.md) |  | [optional] 
**dependent_asset_count** | **int** |  | [optional] 
**metadata** | [**FullMetadata**](FullMetadata.md) |  | [optional] 
**impact_level** | **str** |  | [optional] 
**categories** | [**list[MinimalCategory]**](MinimalCategory.md) |  | [optional] 
**subtype** | **str** |  | 
**host_name** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**cpu_count** | **int** |  | [optional] 
**ram** | **int** |  | [optional] 
**architecture** | **str** |  | [optional] 
**bits** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**remote_access_capable** | **bool** |  | [optional] 
**remote_access_templates** | [**list[MinimalRemoteAccessTemplate]**](MinimalRemoteAccessTemplate.md) |  | [optional] 
**base_disks** | [**list[FullDisk]**](FullDisk.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


