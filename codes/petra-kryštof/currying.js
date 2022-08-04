// Curry JavaScript version


// g(a, b) => a + b 
// g(a) => h(b) => a + b 

// f(...n)
// f1(n1) ... f2(n2) ... fn(n2)
// f1(n1)(n2)(n2)

function f1(n1) {
    // n1 in scope
    return function f2(n2) {
        // n2 in scope
        return function f3(n3) {
            return n1 + n2 + n3
        }
    }
} 

let f = (n1) => {
    (n2) => {
        (n3) => n1 + n2 + n3
    } 
}

console.log(
    f1(1)(2)(3)
)


