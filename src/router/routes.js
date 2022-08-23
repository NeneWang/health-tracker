
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/IndexPage.vue') },
      { path: '/profile', component: () => import('pages/Profile.vue') },
      { path: '/stats', component: () => import('pages/Stats.vue') },
      { path: '/modify', component: () => import('pages/Modify.vue') },
      { path: '/social', component: () => import('pages/Social.vue') },
    ]
  },

// Always leave this as last one,
// but you can also remove it
{
  path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
}
]

export default routes
