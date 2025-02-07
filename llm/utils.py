# from langchain_neo4j.graphs.neo4j_graph import Neo4jGraph
from langchain_neo4j.graphs import neo4j_graph
import requests


def load_query(graph):
    try:
        # url = "https://gist.githubusercontent.com/tomasonjo/08dc8ba0e19d592c4c3cde40dd6abcc3/raw/da8882249af3e819a80debf3160ebbb3513ee962/microservices.json"
        # import_query = requests.get(url).json()["query"]

        import_query = """
          CREATE 
            (catalog:Microservice {name: 'CatalogService', technology: 'Java'}),
            (order:Microservice {name: 'OrderService', technology: 'Python'}),
            (user:Microservice {name: 'UserService', technology: 'Go'}),
            (payment:Microservice {name: 'PaymentService', technology: 'Node.js'}),
            (inventory:Microservice {name: 'InventoryService', technology: 'Java'}),
            (shipping:Microservice {name: 'ShippingService', technology: 'Python'}),
            (review:Microservice {name: 'ReviewService', technology: 'Go'}),
            (recommendation:Microservice {name: 'RecommendationService', technology: 'Node.js'}),
            (auth:Microservice {name: 'AuthService', technology: 'Node.js'}),
            (db:Dependency {name: 'Database', type: 'SQL'}),
            (cache:Dependency {name: 'Cache', type: 'In-memory'}),
            (mq:Dependency {name: 'MessageQueue', type: 'Pub-Sub'}),
            (api:Dependency {name: 'ExternalAPI', type: 'REST'}),
            (bugFixCatalog:Task {name: 'BugFix', description: 'Fix bug in CatalogService', status: 'OPEN'}),
            (featureAddOrder:Task {name: 'FeatureAdd', description: 'Add feature to OrderService', status: 'IN PROGRESS'}),
            (refactorUser:Task {name: 'Refactor', description: 'Refactor UserService', status: 'COMPLETED'}),
            (optimizePayment:Task {name: 'Optimize', description: 'Optimize PaymentService', status: 'OPEN'}),
            (updateInventory:Task {name: 'Update', description: 'Update InventoryService', status: 'IN PROGRESS'}),
            (enhanceShipping:Task {name: 'Enhance', description: 'Enhance ShippingService', status: 'COMPLETED'}),
            (reviewFix:Task {name: 'ReviewFix', description: 'Fix ReviewService', status: 'OPEN'}),
            (recommendationFeature:Task {name: 'RecommendationFeature', description: 'Add feature to RecommendationService', status: 'IN PROGRESS'}),
            (optimizeAuth:Task {name: 'Optimize', description: 'Optimize AuthService', status: 'OPEN'}),
            (teamA:Team {name: 'TeamA'}),
            (teamB:Team {name: 'TeamB'}),
            (teamC:Team {name: 'TeamC'}),
            (teamD:Team {name: 'TeamD'}),
            (alice:Person {name: 'Alice'}),
            (bob:Person {name: 'Bob'}),
            (charlie:Person {name: 'Charlie'}),
            (diana:Person {name: 'Diana'}),
            (eva:Person {name: 'Eva'}),
            (frank:Person {name: 'Frank'}),
            (catalog)-[:DEPENDS_ON]->(db),
            (order)-[:DEPENDS_ON]->(db),
            (user)-[:DEPENDS_ON]->(db),
            (payment)-[:DEPENDS_ON]->(db),
            (inventory)-[:DEPENDS_ON]->(db),
            (shipping)-[:DEPENDS_ON]->(mq),
            (review)-[:DEPENDS_ON]->(cache),
            (recommendation)-[:DEPENDS_ON]->(api),
            (auth)-[:DEPENDS_ON]->(db),
            (order)-[:DEPENDS_ON]->(inventory),
            (order)-[:DEPENDS_ON]->(shipping),
            (order)-[:DEPENDS_ON]->(payment),
            (catalog)-[:DEPENDS_ON]->(review),
            (catalog)-[:DEPENDS_ON]->(recommendation),
            (user)-[:DEPENDS_ON]->(auth),
            (payment)-[:DEPENDS_ON]->(auth),
            (shipping)-[:DEPENDS_ON]->(auth),
            (catalog)-[:MAINTAINED_BY]->(teamA),
            (order)-[:MAINTAINED_BY]->(teamB),
            (user)-[:MAINTAINED_BY]->(teamC),
            (payment)-[:MAINTAINED_BY]->(teamD),
            (inventory)-[:MAINTAINED_BY]->(teamA),
            (shipping)-[:MAINTAINED_BY]->(teamB),
            (review)-[:MAINTAINED_BY]->(teamC),
            (recommendation)-[:MAINTAINED_BY]->(teamD),
            (auth)-[:MAINTAINED_BY]->(teamA),
            (bugFixCatalog)-[:ASSIGNED_TO]->(teamA),
            (featureAddOrder)-[:ASSIGNED_TO]->(teamB),
            (refactorUser)-[:ASSIGNED_TO]->(teamC),
            (optimizePayment)-[:ASSIGNED_TO]->(teamD),
            (updateInventory)-[:ASSIGNED_TO]->(teamA),
            (enhanceShipping)-[:ASSIGNED_TO]->(teamB),
            (reviewFix)-[:ASSIGNED_TO]->(teamC),
            (recommendationFeature)-[:ASSIGNED_TO]->(teamD),
            (optimizeAuth)-[:ASSIGNED_TO]->(teamA),
            (bugFixCatalog)-[:LINKED_TO]->(catalog),
            (featureAddOrder)-[:LINKED_TO]->(order),
            (refactorUser)-[:LINKED_TO]->(user),
            (optimizePayment)-[:LINKED_TO]->(payment),
            (updateInventory)-[:LINKED_TO]->(inventory),
            (enhanceShipping)-[:LINKED_TO]->(shipping),
            (reviewFix)-[:LINKED_TO]->(review),
            (recommendationFeature)-[:LINKED_TO]->(recommendation),
            (optimizeAuth)-[:LINKED_TO]->(auth),
            (alice)-[:MEMBER_OF]->(teamA),
            (bob)-[:MEMBER_OF]->(teamB),
            (charlie)-[:MEMBER_OF]->(teamC),
            (diana)-[:MEMBER_OF]->(teamD),
            (eva)-[:MEMBER_OF]->(teamA),
            (frank)-[:MEMBER_OF]->(teamB),
            (alice)-[:LEAD_OF]->(teamA),
            (bob)-[:LEAD_OF]->(teamB),
            (charlie)-[:LEAD_OF]->(teamC),
            (diana)-[:LEAD_OF]->(teamD)
        """
        graph.query(import_query)
        return True
    except:
        return False


def get_graph(url, username, password):
    return neo4j_graph(url=url, username=username, password=password)

if __name__ == "__main__":
    url = "bolt://localhost:7687"
    username = "neo4j"
    password = "12345678"

    graph = get_graph(url, username, password)
    load_query(graph)