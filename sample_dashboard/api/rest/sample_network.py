# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""sample API over neutron 
"""

from openstack_dashboard.api import neutron
from openstack_dashboard.api.rest import urls
from openstack_dashboard.api.rest import utils as rest_utils

@urls.register
class SampleNetwork(generic.Views):
    """API for load balancers.
    """
    url_regex = r'sample-network/networks/$'

    @rest_utils.ajax()
    def get(self, request):
        """List networks for current project.
        The listing result is an object with property "items".
        """
        # tenant_id = request.user.project_id
        # loadbalancers = neutronclient(request).list_loadbalancers(
        #     tenant_id=tenant_id).get('loadbalancers')
        # if request.GET.get('full') and network.floating_ip_supported(request):
        #     add_floating_ip_info(request, loadbalancers)
        loadbalancers = neutron.network_list(request)
        return {'items': loadbalancers}
