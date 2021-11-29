use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let notas: Vec<i64> = vec![100, 50, 20, 10, 5, 2, 1];

	stdin.read_line(&mut buffer)?;
	let mut valor: i64 = buffer.trim().parse()?;

	println!("{}", valor);

	for nota in notas {
		let qt: i64 = valor / nota;
		valor %= nota;

		println!("{} nota(s) de R$ {},00", qt, nota);
	}

	Ok(())
}