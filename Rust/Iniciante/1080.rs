use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let mut m: i64 = 0;
	let mut p: i64 = 0;

	for i in 0..100 {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let n: i64 = buffer.trim().parse()?;

		if n > m {
			m = n;
			p = i;
		}
	}

	println!("{}", m);
	println!("{}", p + 1);

	Ok(())
}