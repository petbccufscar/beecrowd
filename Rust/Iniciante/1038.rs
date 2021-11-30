use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
	let stdin = io::stdin();
	let mut buffer = String::new();

	let produtos: Vec<f64> = vec![4.0, 4.5, 5.0, 2.0, 1.5];

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let codigo: i64 = tokens.next().unwrap().parse()?;
	let quantidade: i64 = tokens.next().unwrap().parse()?;

	let total: f64 = produtos[(codigo - 1) as usize] * quantidade as f64;

	println!("Total: R$ {:.2}", total);

	Ok(())
}