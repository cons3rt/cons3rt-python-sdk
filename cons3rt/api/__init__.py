"""
   Copyright 2020 Jackpine Technologies Corporation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from __future__ import absolute_import

# flake8: noqa

# import apis into api package
from cons3rt.api.assets_api import AssetsApi
from cons3rt.api.categories_api import CategoriesApi
from cons3rt.api.client_api import ClientApi
from cons3rt.api.clouds_api import CloudsApi
from cons3rt.api.compositions_api import CompositionsApi
from cons3rt.api.container_assets_api import ContainerAssetsApi
from cons3rt.api.deployment_runs_api import DeploymentRunsApi
from cons3rt.api.deployments_api import DeploymentsApi
from cons3rt.api.import_api import ImportApi
from cons3rt.api.projects_api import ProjectsApi
from cons3rt.api.scenarios_api import ScenariosApi
from cons3rt.api.software_assets_api import SoftwareAssetsApi
from cons3rt.api.software_bundles_api import SoftwareBundlesApi
from cons3rt.api.system_assets_api import SystemAssetsApi
from cons3rt.api.systems_api import SystemsApi
from cons3rt.api.teams_api import TeamsApi
from cons3rt.api.templates_api import TemplatesApi
from cons3rt.api.test_assets_api import TestAssetsApi
from cons3rt.api.test_tools_api import TestToolsApi
from cons3rt.api.upload_api import UploadApi
from cons3rt.api.users_api import UsersApi
from cons3rt.api.virtualization_realms_api import VirtualizationRealmsApi
from cons3rt.api.default_api import DefaultApi


__author__ = 'Jackpine Technologies Corporation'
__copyright__ = 'Copyright 2020, Jackpine Technologies Corporation'
__license__ = 'Apache 2.0',
__version__ = '1.0.0'
__maintainer__ = 'API Support'
__email__ = 'support@cons3rt.com'