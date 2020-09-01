import deqaf from 'https://unpkg.com/deqaf/index.js'

function nthLetter(selector, index, rule) {
  return Array.from(document.querySelectorAll(selector))
    .reduce((styles, tag, count) => {
      const attr = selector.replace(/\W/g, '')
      if (
        !tag.dataset.split
        && !tag.children.length
      ) {
        tag.innerHTML = tag.textContent
          .split(' ')
          .map(word => `<span data-word>${
            word.replace(/\S/g, '<span data-letter>$&</span>')
          }</span>`)
          .join(' ')
        tag.dataset.split = true
      }
      tag.querySelectorAll('[data-letter]')[index - 1].setAttribute(`data-nthletter-${attr}`, count)
      styles += `[data-nthletter-${attr}="${count}"] { ${rule} }\n`
      return styles
    }, '')
}

function nthWord(selector, index, rule) {
  return Array.from(document.querySelectorAll(selector))
    .reduce((styles, tag, count) => {
      const attr = selector.replace(/\W/g, '')
      if (
        !tag.dataset.split
        && !tag.children.length
      ) {
        tag.innerHTML = tag.textContent
          .split(' ')
          .map(word => `<span data-word>${
            word.replace(/\S/g, '<span data-letter>$&</span>')
          }</span>`)
          .join(' ')
        tag.dataset.split = true
      }
      tag.setAttribute(`data-nthword-${attr}`, count)
      styles += `[data-nthword-${attr}="${count}"] [data-word]:nth-of-type(${index}) { ${rule} }\n`
      return styles
    }, '')
}

deqaf({
  stylesheet: {},
  rule: {
    nthLetter,
    nthWord
  }
})