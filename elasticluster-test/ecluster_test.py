import elasticluster


cloud_provider = elasticluster.GoogleCloudProvider('388332787657-b8nkuancpbn9njih50697sd274kca496.apps.googleusercontent.com',
                                         'cXnZN7e-z_vO6gVm6ou9D34X', 'spry-notch-318823')


groups = dict()
groups['frontend'] = ['gridengine_master']
groups['compute'] = ['gridengine_worker']

setup_provider = elasticluster.AnsibleSetupProvider(groups)

cluster = elasticluster.Cluster('python-ecluster', cloud_provider,
                                setup_provider, 'elasticluster',
                                '~/.ssh/google_compute_engine',
                                '~/.ssh/google_compute_engine.pub')


cluster.add_node('frontend', 'ubuntu-1604-xenial-v20190913', 'ziygawish',
                'g1-small', 'default')


cluster.add_nodes('compute', 2, 'ubuntu-1604-xenial-v20190913', 'ziygawish',
                'g1-small', 'default')


cluster.start()

cluster.setup()