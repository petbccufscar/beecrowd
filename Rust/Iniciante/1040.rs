use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdio = io::stdin();
	let mut buffer = String::new();

	stdio.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let n1: f64 = tokens.next().unwrap().parse()?;
	let n2: f64 = tokens.next().unwrap().parse()?;
	let n3: f64 = tokens.next().unwrap().parse()?;
	let n4: f64 = tokens.next().unwrap().parse()?;

	let media: f64 = (n1 * 2.0 + n2 * 3.0 + n3 * 4.0 + n4) / 10.0;

	println!("Media: {:.1}", media);

	if media >= 7.0 {
		println!("Aluno aprovado.");
	} else if media >= 5.0 {
		println!("Aluno em exame.");

		buffer.clear();
		stdio.read_line(&mut buffer)?;
		let exame: f64 = buffer.trim().parse()?;

		println!("Nota do exame: {:.1}", exame);

		let media_final: f64 = (media + exame) / 2.0;

		if media_final >= 5.0 {
			println!("Aluno aprovado.");
		} else {
			println!("Aluno reprovado.");
		}

		println!("Media final: {:.1}", media_final);
	} else {
		println!("Aluno reprovado.");
	}

	Ok(())
}