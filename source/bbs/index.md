---
title: bbs
date: 2018-05-30 13:00:00
---

## Leave a comment and share your view :)

![Konata](https://user-images.githubusercontent.com/12698567/40700912-4b2c5824-640e-11e8-9694-7a212f66dc7e.jpg)


<div id="container"></div>
<link rel="stylesheet" href="https://imsun.github.io/gitment/style/default.css">
<script src="https://imsun.github.io/gitment/dist/gitment.browser.js"></script>
<script>
const myTheme = {
  render(state, instance) {
    const container = document.createElement('div')
    container.lang = "en-US"
    container.className = 'gitment-container gitment-root-container'
    
     // your custom component
    container.appendChild(instance.renderSomething(state, instance))
    
    container.appendChild(instance.renderHeader(state, instance))
    container.appendChild(instance.renderEditor(state, instance))
    container.appendChild(instance.renderComments(state, instance))
    container.appendChild(instance.renderFooter(state, instance))
    return container
  },
  renderSomething(state, instance) {
    const container = document.createElement('div')
    container.lang = "en-US"
    if (state.user.login) {
      container.innerText = `Hello, ${state.user.login}`
    }
    return container
  }
}

var gitment = new Gitment({
  owner: 'GooZy',
  repo: 'GooZy.github.io',
  oauth: {
    client_id: '09ad28d84613270d54c9',
    client_secret: '7de5d1666c4a92e382ccbfd05735a7d468f06ddf',
  },
  theme: myTheme,
})
gitment.render('container')
</script>