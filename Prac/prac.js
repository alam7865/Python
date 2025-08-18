// function fun() {
//   for (let i = 1; i <= 5; i++) {
//     setTimeout(() => {
//       console.log(i);
//     }, i * 1000);
//   }
// }

// fun();

// ////////////////// print 1 to 5 after 1 second using var //////////////////

function fun() {
  for (var i = 1; i <= 5; i++) {
    function clse(num) {
      setTimeout(() => {
        console.log(num);
      }, num * 1000);
    }

    clse(i);
  }
}

fun();
