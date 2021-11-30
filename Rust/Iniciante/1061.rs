use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let di: i64 = buffer.trim().replace("Dia ", "").parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.trim().split(" : ");

	let hi: i64 = tokens.next().unwrap().parse()?;
	let mi: i64 = tokens.next().unwrap().parse()?;
	let si: i64 = tokens.next().unwrap().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let df: i64 = buffer.trim().replace("Dia ", "").parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.trim().split(" : ");

	let hf: i64 = tokens.next().unwrap().parse()?;
	let mf: i64 = tokens.next().unwrap().parse()?;
	let sf: i64 = tokens.next().unwrap().parse()?;

	let mut dd: i64 = df - di;
	let mut hd: i64 = hf - hi;
	let mut md: i64 = mf - mi;
	let mut sd: i64 = sf - si;

	if sd < 0 {
		sd += 60;
		md -= 1;
	}

	if md < 0 {
		md += 60;
		hd -= 1;
	}

	if hd < 0 {
		hd += 24;
		dd -= 1;
	}

	println!("{} dia(s)", dd);
	println!("{} hora(s)", hd);
	println!("{} minuto(s)", md);
	println!("{} segundo(s)", sd);

	Ok(())
}