window.addEventListener("scroll", ()=>{
    document.querySelector('nav').classList.toggle('window-scroll', window.scrollY >0)

})

const faqs=document.querySelectorAll('.faq')

faqs.forEach(faq => {
    faq.addEventListener('click', ()=>{
        faq.classList.toggle('open');
    })

    const icon=faq.querySelector('.faq_icon i');

    if(icon.className=='fa fa-minus'){
        icon.className="fa fa-minus";
    }else{
        icon.className="fa fa-plus";
    }
        
});