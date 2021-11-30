use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let mut pares = 0;
	let mut impares = 0;
	let mut positivos = 0;
	let mut negativos = 0;

	for _ in 0..5 {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		
		let n: i64 = buffer.trim().parse()?;

		if n % 2 == 0 {
			pares += 1;
		} else {
			impares += 1;
		}

		if n > 0 {
			positivos += 1;
		} else if n < 0 {
			negativos += 1;
		}
	}

	println!("{} valor(es) par(es)", pares);
	println!("{} valor(es) impar(es)", impares);
	println!("{} valor(es) positivo(s)", positivos);
	println!("{} valor(es) negativo(s)", negativos);

	Ok(())
}