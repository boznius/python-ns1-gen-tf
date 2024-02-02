resource "ns1_zone" "example_domain.com" {
  zone = "example_domain.com"
}

resource "ns1_record" "example_domain.com" {
  zone = "example_domain.com"
  domain = "example_domain.com"
  type = "NS"
  answers = []
}

resource "ns1_record" "jacktest.example_domain.com" {
  zone = "example_domain.com"
  domain = "jacktest.example_domain.com"
  type = "CNAME"
  answers = []
}

resource "ns1_record" "jiktak.example_domain.com" {
  zone = "example_domain.com"
  domain = "jiktak.example_domain.com"
  type = "A"
  answers = []
}

