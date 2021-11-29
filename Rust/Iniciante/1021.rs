use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let notas: Vec<i64> = vec![10000, 5000, 2000, 1000, 500, 200];
	let moedas: Vec<i64> = vec![100, 50, 25, 10, 5, 1];

	stdin.read_line(&mut buffer)?;
	let valor: f64 = buffer.trim().parse()?;
	let mut valor: i64 = (valor * 100.0) as i64;

	println!("NOTAS:");
	for nota in notas {
		let qt: i64 = valor / nota;
		valor %= nota;

		println!("{} nota(s) de R$ {:.2}", qt, nota as f64 / 100.0);
	}

	println!("MOEDAS:");
	for moeda in moedas {
		let qt: i64 = valor / moeda;
		valor %= moeda;

		println!("{} moeda(s) de R$ {:.2}", qt, moeda as f64 / 100.0);
	}

	Ok(())
}