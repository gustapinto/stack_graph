import diagrams as d
import diagrams.programming.flowchart as pfl
import diagrams.programming.framework as pfr
import diagrams.programming.language as pl
import diagrams.onprem.database as od
import diagrams.onprem.workflow as ow
import diagrams.onprem.analytics as oa
import diagrams.onprem.container as oc
import diagrams.onprem.inmemory as oi
import diagrams.onprem.queue as oq
import diagrams.aws.compute as ac
import diagrams.aws.storage as ast
import diagrams.aws.database as ad
import diagrams.gcp.compute as gc
import diagrams.gcp.analytics as ga
import diagrams.gcp.storage as gs
import diagrams.gcp.database as gd

data = {
    'nodes': {
        '2020': {
            'icon': pfl.Inspection,
            'label': '2020',
            'color': 'orange',
            'is_cluster': True,
        },
        '2021': {
            'icon': pfl.Inspection,
            'label': '2021',
            'color': 'red',
            'is_cluster': True,
        },
        '2022': {
            'icon': pfl.Inspection,
            'label': '2022',
            'color': 'green',
            'is_cluster': True,
        },
        '2023': {
            'icon': pfl.Inspection,
            'label': '2023',
            'color': 'darkgreen',
            'is_cluster': True,
        },
        'php': {
            'icon': pl.Php,
        },
        'laravel': {
            'icon': pfr.Laravel,
        },
        'js': {
            'icon': pl.Javascript,
        },
        'mysql': {
            'icon': od.MySQL,
        },
        'python': {
            'icon': pl.Python,
        },
        'flask': {
            'icon': pfr.Flask,
        },
        'postgresql': {
            'icon': od.PostgreSQL,
        },
        'lambda': {
            'icon': ac.Lambda,
        },
        'rds': {
            'icon': ad.RDS,
        },
        's3': {
            'icon': ast.S3,
        },
        'airflow': {
            'icon': ow.Airflow,
        },
        'react': {
            'icon': pfr.React,
        },
        'go': {
            'icon': pl.Go,
        },
        'docker': {
            'icon': oc.Docker,
        },
        'hazelcast': {
            'icon': oi.Hazelcast,
        },
        'redis': {
            'icon': oi.Redis,
        },
        'celery': {
            'icon': oq.Celery,
        },
        'kafka': {
            'icon': oq.Kafka,
        },
        'storage': {
            'icon': gs.Storage,
        },
        'dataproc': {
            'icon': ga.Dataproc,
        },
        'spark': {
            'icon': oa.Spark,
        },
        'functions': {
            'icon': gc.Functions,
        },
        'cloud_run': {
            'icon': gc.Run,
        },
        'cloud_sql': {
            'icon': gd.SQL,
        },
        'pubsub': {
            'icon': ga.PubSub,
        },
        'bigquery': {
            'icon': ga.BigQuery,
        },
        'java': {
            'icon': pl.Java,
        },
    },
    'relationships': [
        {
            'from': '2020',
            'to': [
                'docker',
                'php',
                'laravel',
                'js',
                'mysql',
            ],
        },
        {
            'from': 'php',
            'to': [
                'laravel',
            ],
        },
        {
            'from': 'laravel',
            'to': [
                'mysql',
                'postgresql',
            ],
        },
        {
            'from': '2021',
            'to': [
                'docker',
                'laravel',
                'js',
                'mysql',
                'python',
                'flask',
                'postgresql',
                'lambda',
                'rds',
                's3',
                'celery',
                'redis',
            ],
        },
        {
            'from': 'python',
            'to': [
                'flask',
                'celery',
                'postgresql',
            ],
        },
        {
            'from': 'celery',
            'to': [
                'redis',
            ],
        },
        {
            'from': 'js',
            'to': [
                'lambda',
            ],
        },
        {
            'from': '2022',
            'to': [
                'docker',
                'python',
                'laravel',
                'react',
                'postgresql',
                'airflow',
                'go',
                'hazelcast',
            ],
        },
        {
            'from': 'go',
            'to': [
                'hazelcast',
                'functions',
                'cloud_sql',
                'pubsub',
                'postgresql',
            ],
        },
        {
            'from': 'react',
            'to': [
                'js',
            ],
        },
        {
            'from': 'airflow',
            'to': [
                'python',
            ],
        },
        {
            'from': '2023',
            'to': [
                'docker',
                'python',
                'laravel',
                'react',
                'postgresql',
                'airflow',
                'go',
                'spark',
                'dataproc',
                'storage',
                'functions',
                'kafka',
                'cloud_run',
                'cloud_sql',
                'pubsub',
                'bigquery',
                'java',
            ],
        },
        {
            'from': 'spark',
            'to': [
                'dataproc',
                'kafka',
                'bigquery',
                'pubsub',
                'java',
            ],
        },
    ],
}

def render(from_node: dict) -> None:
    from_icon = (from_node['icon'])(label=from_node.get('label', ''),
                                    nodeid=from_node_id)

    for to_node_id in relationship['to']:
        to_node = data['nodes'][to_node_id]
        to_icon = (to_node['icon'])(label='',
                                                nodeid=to_node_id)

        from_icon >> d.Edge(color=from_node.get('color', '')) >> to_icon


with d.Diagram(name='', curvestyle='curved', direction='TB', filename='graph'):
    for relationship in data['relationships']:
        from_node_id = relationship['from']
        from_node = data['nodes'][from_node_id]

        if from_node.get('is_cluster', False):
            with d.Cluster(label=from_node.get('label', '')):
                render(from_node)
                continue
        else:
            render(from_node)
