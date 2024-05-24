const textareaPhones = document.getElementById('Phones');
const textareaMessage = document.getElementById('Message');

const BtnMilling = document.getElementById('BtnMilling');

const ButtonInputState = () => {
  if (textareaPhones.value && textareaMessage.value) {
    BtnMilling.style.opacity = 1;
  } else {
    BtnMilling.style.opacity = 0.4;
  }
}

textareaPhones.addEventListener('input', ButtonInputState);
textareaMessage.addEventListener('input', ButtonInputState);

textareaPhones.addEventListener('keyup', (e) => {
  textareaPhones.style.height = 'auto';
  let scHeight = e.target.scrollHeight;
  textareaPhones.style.height = scHeight + 'px';
});

textareaMessage.addEventListener('keyup', (e) => {
  textareaMessage.style.height = 'auto';
  let scHeight = e.target.scrollHeight;
  textareaMessage.style.height = scHeight + 'px';
});

const copy__web__whatsapp = document.getElementById('copy__web__whatsapp');
const copy__success = document.getElementById('copy__success');

copy__web__whatsapp.addEventListener('click', (e) => {
  e.preventDefault();

  const copy__text = document.getElementById('copy__text__web__whatsapp');

  copy__text.select();
  navigator.clipboard.writeText(copy__text.value);
  copy__text.blur();

  copy__success.style.display = 'block';
  setTimeout(() => {
    copy__success.style.display = 'none';
    copy__success.classList.add('slide-out-bottom');
  }, 2000);
});

const preloader = document.getElementById('start__app');

window.addEventListener('load', () => {
  preloader.classList.add('hide');
  setTimeout(() => {
    preloader.remove();
  }, 1000);
});

const btnTime = document.getElementById('btn_time');
const time = document.getElementById('time__popUp');

btnTime.addEventListener('click', (e) => {
  e.preventDefault();

  const phones = textareaPhones.value;

  if (phones.length < 1) {
    return;
  }

  const elements = phones.split("\n");
  const count = elements.length;

  const timeResult = count * 12;
  const minutes = Math.floor(timeResult / 60);

  const result = timeResult < 60 ? `${timeResult} сек.` : `${minutes} мин.`;
  document.getElementById('js__time').innerText = result;

  time.style.display = 'block';

  setTimeout(() => {
    time.style.display = 'none';
  }, 5000);
});