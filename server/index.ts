import express from 'express';
import { createHandler } from 'graphql-http/lib/use/express';

const app = express();

app.all('/graphql', createHandler({
  
}));

app.listen(4000, () => {
  console.log('Listening...');
});