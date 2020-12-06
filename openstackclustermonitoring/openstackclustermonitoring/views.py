
from django.http import HttpResponse
from django.shortcuts import render
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as nova_client
from cinderclient import client as cinder_client
from neutronclient.v2_0 import client as neutron_client 
from . import configs
from . import openstack_authen
import json


def index(request):

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)
    #return HttpResponse("<h1>Hello, world. You're at the openstack cluster monitoring index.</h1>")

def site_setting(request):
    return HttpResponse("<h1>Hello, world. You're at the openstack cluster monitoring site setting.</h1>")

def monitor_openstack(request):
    tmp_dic = dict()
    context = dict()
    sess = openstack_authen.initial_nova_connection()
    #print(sess.hypervisors.list())
    for hypervisor in sess.hypervisors.list():
        hostname = hypervisor.hypervisor_hostname
        tmp_dic[hostname] = hypervisor.state
    context['hypervisor']= tmp_dic
     
    tmp_dic = dict()
    for service in sess.services.list():
        #print(str(service.__dict__))
        service_fullname = service.binary + "@" + service.host
        tmp_dic[service_fullname] = service.state
    context['nova_services']= tmp_dic
    
    sess = openstack_authen.initial_cinder_connection()
    tmp_dic = dict()
    for service in sess.services.list():
        #print(str(service.__dict__))
        service_fullname = service.binary + "@" + service.host
        tmp_dic[service_fullname] = service.state
    context['cinder_services']= tmp_dic

    sess = openstack_authen.initial_neutron_connection()
    tmp_dic = dict()
    neutron_agentlist= sess.list_agents()
    #print(neutron_agentlist)
    for agent in neutron_agentlist['agents']:
        print(agent)
        #print(agent['binary'],'@',agent['host'])
        service_fullname = agent['binary'] + "@" + agent['host']
        service_state = "up"
        if agent['alive'] == "False":
            service_state = "down"
        print(service_fullname,service_state)
        tmp_dic[service_fullname] = service_state
        sorted(tmp_dic)
    context['neutron_services']= tmp_dic
    # for service in sess.list_agents():
    #     print(type(service))
        # for p in service.agents:
        #     print(p)
            # for k, v in p.items():
            #     print("%s : %s" % (k, v))
            # print('\n')
    #     service_fullname = service.binary + "@" + service.host
    #     tmp_dic[service_fullname] = service.state
    # context['neuutron_services']= tmp_dic

    print(context)
    return render(request, 'home.html', context=context)
    #return HttpResponse("<h1>Hello, world. You're at the openstack cluster monitoring Openstack monitoring.</h1>")
    


def monitor_ceph(request):
    return HttpResponse("<h1>Hello, world. You're at the openstack cluster monitoring Ceph monitoring.</h1>")