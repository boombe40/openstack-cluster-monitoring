from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as nova_client
from cinderclient import client as cinder_client
from neutronclient.v2_0 import client as neutron_client 
from . import configs

def initial_neutron_connection():
    loader = loading.get_plugin_loader(configs.OS_AUTH_PLUGIN)
    auth = loader.load_from_options(
        username=configs.OS_USERNAME,
        password=configs.OS_PASSWORD,
        project_name=configs.OS_PROJECT_NAME,
        auth_url=configs.OS_AUTH_URL,
        user_domain_name=configs.OS_USER_DOMAIN_NAME,
        project_domain_name=configs.OS_PROJECT_DOMAIN_NAME)
    kwargs = {'endpoint_type': configs.OS_ENDPOINT_TYPE}
    neutron = neutron_client.Client(
                              session=session.Session(auth=auth),
                              **kwargs)
    print("login neutron success")
    return neutron

def initial_nova_connection():
    loader = loading.get_plugin_loader(configs.OS_AUTH_PLUGIN)
    auth = loader.load_from_options(
        username=configs.OS_USERNAME,
        password=configs.OS_PASSWORD,
        project_name=configs.OS_PROJECT_NAME,
        auth_url=configs.OS_AUTH_URL,
        user_domain_name=configs.OS_USER_DOMAIN_NAME,
        project_domain_name=configs.OS_PROJECT_DOMAIN_NAME)
    kwargs = {'endpoint_type': configs.OS_ENDPOINT_TYPE}
    nova = nova_client.Client(version=2,
                              session=session.Session(auth=auth),
                              **kwargs)
    print("login nova success")
    return nova

def initial_cinder_connection():
    loader = loading.get_plugin_loader(configs.OS_AUTH_PLUGIN)
    auth = loader.load_from_options(
        username=configs.OS_USERNAME,
        password=configs.OS_PASSWORD,
        project_name=configs.OS_PROJECT_NAME,
        auth_url=configs.OS_AUTH_URL,
        user_domain_name=configs.OS_USER_DOMAIN_NAME,
        project_domain_name=configs.OS_PROJECT_DOMAIN_NAME)
    kwargs = {'endpoint_type': configs.OS_ENDPOINT_TYPE}
    cinder = cinder_client.Client(version=3,
                              session=session.Session(auth=auth),
                              **kwargs)
    print("login cinder success")
    return cinder