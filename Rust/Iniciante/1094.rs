use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let n: i64 = buffer.trim().parse()?;

	let mut c: i64 = 0;
	let mut r: i64 = 0;
	let mut s: i64 = 0;

	for _ in 0..n {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let mut tokens = buffer.split_whitespace();

		let qt: i64 = tokens.next().unwrap().parse()?;
		let tp: &str = tokens.next().unwrap();

		match tp {
			"C" => c += qt,
			"R" => r += qt,
			"S" => s += qt,
			_ => {}
		}
	}

	let total: i64 = c + r + s;

	println!("Total: {} cobaias", total);
	println!("Total de coelhos: {}", c);
	println!("Total de ratos: {}", r);
	println!("Total de sapos: {}", s);
	println!("Percentual de coelhos: {:.2} %", c as f64 / total as f64 * 100.0);
	println!("Percentual de ratos: {:.2} %", r as f64 / total as f64 * 100.0);
	println!("Percentual de sapos: {:.2} %", s as f64 / total as f64 * 100.0);

	Ok(())
}