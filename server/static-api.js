const worker = new Worker(new URL('./static-worker.js', import.meta.url), {type: 'module'});
const requests = new Map();
let nextId = 0, failure;
worker.onmessage = ({data}) => {
  const pending = requests.get(data.id);
  if (!pending) return;
  pending.cleanup();
  if (data.error) pending.reject(new Error(data.error));
  else pending.resolve(data.result);
};
worker.onerror = () => {
  failure = new Error('搜索线程启动失败，请刷新页面或使用较新的浏览器。');
  for (const pending of requests.values()) {pending.cleanup(); pending.reject(failure);}
};
export function api(route, params = {}, signal) {
  return new Promise((resolve, reject) => {
    if (failure) return reject(failure);
    if (signal?.aborted) return reject(new DOMException('Aborted', 'AbortError'));
    const id = ++nextId;
    const cleanup = () => {requests.delete(id); signal?.removeEventListener('abort', abort);};
    const abort = () => {cleanup(); worker.postMessage({id, cancel: true}); reject(new DOMException('Aborted', 'AbortError'));};
    requests.set(id, {resolve, reject, cleanup});
    signal?.addEventListener('abort', abort, {once: true});
    worker.postMessage({id, route, params});
  });
}
