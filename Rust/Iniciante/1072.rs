use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let n: i64 = buffer.trim().parse()?;

	let mut dentro = 0;
	let mut fora = 0;

	for _ in 0..n {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let x: i64 = buffer.trim().parse()?;

		if 10 <= x && x <= 20 {
			dentro += 1;
		} else {
			fora += 1;
		}
	}

	println!("{} in", dentro);
	println!("{} out", fora);

	Ok(())
}