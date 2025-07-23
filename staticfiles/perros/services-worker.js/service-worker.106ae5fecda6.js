const CACHE_NAME = 'perros-cache-v1';
const urlsToCache = [
  '/',
  '/static/perros/manifest.json',
  '/static/perros/icons/icon-192.png',
  '/static/perros/icons/icon-512.png',
  // Agregá acá otras rutas estáticas que uses, ej. CSS, JS, imágenes
];

// Instalación: cachear archivos esenciales
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// Activación: limpiar caches viejos
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      )
    )
  );
});

// Fetch: responder con cache o hacer fetch a red
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
