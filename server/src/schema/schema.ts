import { GraphQLSchema, GraphQLObjectType, GraphQLString, GraphQLInt } from 'graphql';
import axios from 'axios';

const UserType = new GraphQLObjectType({
  name: 'User',
  fields: {
    id: { type: GraphQLString },
    firstName: { type: GraphQLString },
    age: { type: GraphQLInt },
  },
});

const RootQuery = new GraphQLObjectType({
  name: 'RootQueryType',
  fields: {
    user: {
      type: UserType,
      args: {
        id: { type: GraphQLString },
      },
      resolve(_, args) {
        return axios.get(`http://localhost:3000/users/${args.id}`)
          .then(({ data }) => data);
      }
    },
  },
});

const schema = new GraphQLSchema({
  query: RootQuery,
});

export default schema;
