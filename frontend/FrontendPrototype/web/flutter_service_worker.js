'use strict';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
  "/assets\AssetManifest.json": "86710a29e7571a2e20da8b630e4247d3",
"/assets\assets\img\map.jpg": "8c9af94195e1c387a6c3d1b12a0a3ef9",
"/assets\assets\img\markers.jpg": "9dbfa999f2065e56f5333677718b0f8c",
"/assets\assets\img\preview.jpg": "1aff943c1d0200ccaf5d5fb5771628fe",
"/assets\FontManifest.json": "01700ba55b08a6141f33e168c4a6c22f",
"/assets\fonts\MaterialIcons-Regular.ttf": "56d3ffdef7a25659eab6a68a3fbfaf16",
"/assets\LICENSE": "1dd2889009ed7aab8da76baab41fa094",
"/assets\packages\cupertino_icons\assets\CupertinoIcons.ttf": "115e937bb829a890521f72d2e664b632",
"/index.html": "b5da39e88acd11ddb966858823232919",
"/main.dart.js": "a290b0e8e423504560d5263ecc078f69"
};

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (cacheName) {
      return caches.delete(cacheName);
    }).then(function (_) {
      return caches.open(CACHE_NAME);
    }).then(function (cache) {
      return cache.addAll(Object.keys(RESOURCES));
    })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        if (response) {
          return response;
        }
        return fetch(event.request, {
          credentials: 'include'
        });
      })
  );
});
