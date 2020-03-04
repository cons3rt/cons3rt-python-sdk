# FullAzureVirtualizationRealm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtualization_realm_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**state** | **str** |  | [optional] 
**access_point** | **str** |  | [optional] 
**account_id** | **str** |  | 
**active_virtual_machines** | **int** |  | [optional] 
**networks** | [**list[Network]**](Network.md) |  | 
**admin_users** | [**list[MinimalUser]**](MinimalUser.md) |  | [optional] 
**allocated** | **bool** |  | [optional] 
**cloud** | [**MinimalCloud**](MinimalCloud.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**date_last_reachable** | **datetime** |  | [optional] 
**description** | **str** |  | 
**default_windows_domain_name** | **str** |  | [optional] 
**local_storage_name** | **str** |  | [optional] 
**maximum_impact_level** | **str** |  | [optional] 
**maximum_num_cpus** | **int** |  | [optional] 
**maximum_num_gpus** | **int** |  | [optional] 
**maximum_ram_in_megabytes** | **int** |  | [optional] 
**maximum_storage_in_megabytes** | **int** |  | [optional] 
**maximum_virtual_machines** | **int** |  | [optional] 
**power_on_delay_base** | **int** |  | [optional] 
**power_on_initial_delay_base** | **int** |  | [optional] 
**power_on_minimum_delay** | **int** |  | [optional] 
**projects** | [**list[MinimalProject]**](MinimalProject.md) |  | [optional] 
**reachable** | **bool** |  | [optional] 
**remote_access_config** | [**RemoteAccessConfig**](RemoteAccessConfig.md) |  | [optional] 
**remote_access_deployment_id** | **int** |  | [optional] 
**remote_access_deployment_run_status** | **str** |  | [optional] 
**remote_access_status** | **str** |  | [optional] 
**supported_features** | **list[str]** |  | [optional] 
**template_registrations** | [**list[MinimalTemplateRegistration]**](MinimalTemplateRegistration.md) |  | [optional] 
**templates** | [**list[MinimalCons3rtTemplateData]**](MinimalCons3rtTemplateData.md) |  | [optional] 
**template_subscriptions** | [**list[MinimalTemplateSubscription]**](MinimalTemplateSubscription.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**username** | **str** |  | 
**zone_count** | **int** |  | [optional] 
**environment** | **str** |  | 
**public_container_url** | **str** |  | [optional] 
**region** | **str** |  | 
**resource_group_name** | **str** |  | 
**tenant_id** | **str** |  | 
**virtual_network_name** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


