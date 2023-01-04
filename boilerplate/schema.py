import graphene

import accounts.graphql.schema
import accounts.graphql.mutations


class Query(accounts.graphql.schema.Query, graphene.ObjectType):
    pass

class Mutation(accounts.graphql.mutations.Mutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
