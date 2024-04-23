import express from 'express';
import { createHandler } from 'graphql-http/lib/use/express';
import expressPlayground from 'graphql-playground-middleware-express';

import schema from './src/schema/schema';

const app = express();

app.all('/graphql', createHandler({
  schema,
}));
app.get('/playground', expressPlayground({ endpoint: '/graphql' }));

app.listen(4000, () => {
  console.log('Listening...');
});