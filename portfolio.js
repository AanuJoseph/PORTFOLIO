const loader = document.getElementById('loader')

window.addEventListener('load', () => {
    if (!loader) return
    setTimeout(() => {
        loader.classList.add('hidden')
    }, 1200)
})

if (performance.getEntriesByType('navigation')[0]?.type === 'navigate') {
    document.body.style.overflow = 'hidden'
    setTimeout(() => {
        document.body.style.overflow = ''
    }, 1500)
}

const contactForm = document.getElementById('contactForm')

if (contactForm) {
    contactForm.addEventListener('submit', () => {
        setTimeout(() => {
            contactForm.reset()
        }, 100)
    })
}

let menuIcon = document.querySelector('#menu-icon')
let navbar = document.querySelector('.navbar')

menuIcon.onclick = () => {
    menuIcon.classList.toggle('fa-bars')
    menuIcon.classList.toggle('fa-xmark')
    navbar.classList.toggle('active')
}

let sections = document.querySelectorAll('section')
let navLinks = document.querySelectorAll('header nav a')

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150
        let height = sec.offsetHeight
        let id = sec.getAttribute('id')

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active')
                const target = document.querySelector('header nav a[href*="' + id + '"]')
                if (target) target.classList.add('active')
            })
        }
    })

    let header = document.querySelector('header')
    header.classList.toggle('sticky', window.scrollY > 100)

    if (window.innerWidth <= 768) {
        menuIcon.classList.remove('fa-xmark')
        menuIcon.classList.add('fa-bars')
        navbar.classList.remove('active')
    }
}

ScrollReveal({
    distance: '80px',
    duration: 2000,
    delay: 200
})

ScrollReveal().reveal('.home-content, .heading', { origin: 'top' })
ScrollReveal().reveal('.home-visual, .services-container, .portfolio-container, .contact form', { origin: 'bottom' })
ScrollReveal().reveal('.about-image, .about-content', { origin: 'left' })

const typed = new Typed('.multiple-text', {
    strings: ['React interfaces', 'accessible products', 'clean design systems', 'faster frontends'],
    typeSpeed: 90,
    backSpeed: 80,
    backDelay: 1200,
    loop: true
})
