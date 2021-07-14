import elasticluster

# Initialise an EC2 compatible cloud provider, in this case an OpenStack
# cloud operator is chosen. To initialise the cloud provider the
# following parameters are passed:
#   url:        url to connecto to the cloud operator web service
#   region:     region to start the nodes on
#   access_key: access key of the current user to connect
#   secret_key: secret key of the current user to connect
cloud_provider = elasticluster.providers.gce.GoogleCloudProvider('388332787657-b8nkuancpbn9njih50697sd274kca496.apps.googleusercontent.com',
                                         'cXnZN7e-z_vO6gVm6ou9D34X', 'spry-notch-318823')

# Initialising the setup provider needs a little more preparation:
# the groups dictionary specifies the kind of nodes used for this cluster.
# In this case we want a frontend and a compute kind. The frontend node
# (s) will be setup as slurm_master, the compute node(s) as slurm_worker.
# This corresponds to the documentation of the ansible playbooks
# provided with elasticluster. The kind of the node is a name specified
# by the user. This name will be used to set a new hostname on the
# instance, therefore it should meet the requirements of RFC 953
# groups['kind'] = ['andible_group1', 'ansible_group2']
groups = dict()
groups['frontend'] = ['gridengine_master']
groups['compute'] = ['gridengine_worker']

setup_provider = elasticluster.AnsibleSetupProvider(groups)

# cluster initialisation (note: ssh keys are same for all nodes)
# After the steps above initialising an empty cluster is a peace of cake.
# The cluster takes the following arguments:
# name:           name to identify the cluster
#   cloud_provider: cloud provider to connect to cloud
#   setup_provider: setup provider to configure the cluster
#   ssh_key_name:   name of the ssh key stored (or to be stored) on the
#                   cloud
#   ssh_key_pub:    path to public ssh key file
#   ssh_key_priv:   path to private ssh key file
#
# The ssh key files are used for all instances in this cluster.
cluster = elasticluster.Cluster('python-ecluster', cloud_provider,
                                setup_provider, 'elasticluster',
                                '~/.ssh/google_compute_engine',
                                '~/.ssh/google_compute_engine.pub')

# To add nodes to the cluster we can use the add_node. This
# only initialises a new node, but does not start it yet.
# The add node function is basically a factory method to make it easy to
# add nodes to a cluster. It takes the following arguments:
#   kind:   kind of the node in this cluster. This corresponds to the
#           groups defined in the cloud_provider.
cluster.add_node('frontend', 'ubuntu-1604-xenial-v20190913', 'ziygawish',
                 'g1-small', 'default')

# We can also add multiple nodes with the add_nodes method.
# The following command will add 2 nodes of the kind `compute` to the
# cluster
cluster.add_nodes('compute', 2, 'ubuntu-1604-xenial-v20190913', 'ziygawish',
                 'g1-small', 'default')

# Since we initialised all the nodes for this computing cluster,
# we can finally start the cluster.
# The start method is blocking and does the following tasks:
#   * call the cloud provider to start an instance for each node in a
#     seperate thread.
#   * to make sure elasticluster is not stopped during creation of an
#     instance, it will overwrite the sigint handler
#   * waits until all nodes are alive (meaning ssh connection
#     works)
#   * If the startup timeout is reached and not all nodes are alive,
#     the cluster will stop and destroy all instances
cluster.start()

# Now, all the nodes are started and we can call the setup method to
# configure slurm on the nodes.
cluster.setup()