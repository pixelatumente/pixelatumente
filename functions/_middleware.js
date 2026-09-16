export async function onRequest(context) {
  const { request, next } = context
  const url = new URL(request.url)
  if (url.hostname === 'www.pixelatumente.es') {
    return Response.redirect(`https://pixelatumente.es${url.pathname}${url.search}`, 301)
  }
  return next()
}
