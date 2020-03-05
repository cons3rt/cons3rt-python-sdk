# AzureVirtualizationRealm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtualization_realm_type** | **str** |  | [optional] 
**access_point** | **str** |  | [optional] 
**account_id** | **str** |  | 
**active_virtual_machines** | **int** |  | [optional] 
**networks** | [**list[Network]**](Network.md) |  | [optional] 
**admin_users** | [**list[User]**](User.md) |  | [optional] 
**allocated** | **bool** |  | [optional] 
**cidr** | **str** |  | 
**cloud** | [**Cloud**](Cloud.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**date_last_reachable** | **int** |  | [optional] 
**default_windows_domain_name** | **str** |  | [optional] 
**description** | **str** |  | 
**id** | **int** |  | [optional] 
**local_storage_name** | **str** |  | [optional] 
**maximum_num_cpus** | **int** |  | [optional] 
**maximum_num_gpus** | **int** |  | [optional] 
**maximum_ram_in_megabytes** | **int** |  | [optional] 
**maximum_storage_in_megabytes** | **int** |  | [optional] 
**maximum_virtual_machines** | **int** |  | [optional] 
**name** | **str** |  | 
**password** | **str** |  | 
**power_on_delay_base** | **int** |  | [optional] 
**power_on_initial_delay_base** | **int** |  | [optional] 
**power_on_minimum_delay** | **int** |  | [optional] 
**projects** | [**list[Project]**](Project.md) |  | [optional] 
**reachable** | **bool** |  | [optional] 
**remote_access_config** | [**RemoteAccessConfig**](RemoteAccessConfig.md) |  | [optional] 
**remote_access_deployment_id** | **int** |  | [optional] 
**remote_access_deployment_run_status** | **str** |  | [optional] 
**remote_access_status** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**supported_features** | **list[str]** |  | [optional] 
**template_registrations** | [**list[TemplateRegistration]**](TemplateRegistration.md) |  | [optional] 
**templates** | [**list[Cons3rtTemplateData]**](Cons3rtTemplateData.md) |  | [optional] 
**template_subscriptions** | [**list[TemplateSubscription]**](TemplateSubscription.md) |  | [optional] 
**updated_at** | **int** |  | [optional] 
**username** | **str** |  | 
**zone_count** | **int** |  | [optional] 
**environment** | **str** |  | 
**public_container_url** | **str** |  | [optional] 
**region** | **str** |  | 
**resource_group_name** | **str** |  | 
**tenant_id** | **str** |  | 
**virtual_network_name** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


