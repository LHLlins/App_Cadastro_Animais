async function carregar_animais(){

   const response = await axios.get('http://localhost:8000/animal/')
  
   const animais = response.data 
  
   const lista  = document.getElementById('lista_de_animais')

   animais.forEach(animal => 
         {const item = document.createElement('li')
         item.innerText = animal.nome
         lista.appendChild(item)});

  

}

function manipular_formulario(){
    const form_animal = document.getElementById('form_animal')
    const input_nome = document.getElementById('nome')
    form_animal.onsubmit = async (event)=>{
        event.preventDefault()
        const nome_animal = input_nome.value
        await axios.post('http://localhost:8000/animais', {
            nome : nome_animal,
            idade : 2,
            sexo  : 'male',
            cor :  'blue'
        })
    }

}

function app(){
console.log('App iniciada!!')
carregar_animais()
manipular_formulario()
}
app()