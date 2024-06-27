let tg = window.Telegram.WebApp
const chatIcon = document.querySelectorAll("svg")
const contentBlock = document.querySelector(".content")
const navMenu = document.querySelectorAll(".menu-link")

async function getPage(url) {
  const response = await fetch(url);
  return await response.text();
}

async function menuClick(elem) {
  let reg = /gray.png$/;
  for (i=0; i < navMenu.length; i++) {
    navMenu[i].lastElementChild.classList.remove("menu-icon-name-active")
    const elemSrc = navMenu[i].firstElementChild.src;
    if (!reg.test(elemSrc)) {
      navMenu[i].firstElementChild.src = elemSrc.replace("gradient.png", "gray.png");
    }   
  }
  let src = elem.firstElementChild.src;
  elem.lastElementChild.classList.add("menu-icon-name-active")
  elem.firstElementChild.src = src.replace("gray.png", "gradient.png");
}

async function locationResolver (location, elem) {
  switch (location) {
    case "#/":
      await menuClick(elem)
      const text_main = await getPage('refs.html')
      contentBlock.innerHTML = text_main
      break;
    case "#/feedbacks/":
      await menuClick(elem)
      const text_feedback = await getPage('feedbacks.html')
      contentBlock.innerHTML = text_feedback
      break;
    case "#/balance/":
      await menuClick(elem)
      const text_balanse = await getPage('balance.html')
      contentBlock.innerHTML = text_balanse
      break;
    case "#/account/":
      await menuClick(elem)
      const text_account = await getPage('account.html')
      contentBlock.innerHTML = text_account
      break;
  }
}

window.addEventListener('load', async () => {
  const location = window.location.hash

  if (location) {
    await locationResolver(location)
  }
})