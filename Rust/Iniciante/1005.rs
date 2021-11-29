use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let a: f64 = buffer.trim().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let b: f64 = buffer.trim().parse()?;

	let media: f64 = (a * 3.5 + b * 7.5) / 11.0;

	println!("MEDIA = {:.5}", media);

	Ok(())
}