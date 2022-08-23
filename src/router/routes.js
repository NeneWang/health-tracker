
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: '/stats', componment: () => import('pages/Stats.vue') },
      { path: '/modify', componment: () => import('pages/Modify.vue') },
      { path: '/profile', componment: () => import('pages/Profile.vue') },
      { path: '/social', componment: () => import('pages/Social.vue') },
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
