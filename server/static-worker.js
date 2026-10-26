import {StaticData} from './static-data.js';
const data = new StaticData(new URL('./', import.meta.url));
const requests = new Map();
self.onmessage = async ({data: message}) => {
  const {id, route, params, cancel} = message;
  if (cancel) {requests.get(id)?.abort(); return;}
  const controller = new AbortController();
  requests.set(id, controller);
  try {
    const result = await data.api(route, params, controller.signal);
    if (!controller.signal.aborted) self.postMessage({id, result});
  } catch (error) {
    if (!controller.signal.aborted) self.postMessage({id, error: error.message});
  } finally {requests.delete(id);}
};
