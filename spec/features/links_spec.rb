# spec/features/links_spec.rb
# Demo:
# bin/rspec spec/features/links_spec.rb

# I should have executable:
# chromedriver
# in my path.
# I put it here: ~/bin/chromedriver

require 'rails_helper'

describe 'This should start Chrome', :js => true do
  it 'should visit some links' do
    visit '/'
    sleep 2
    visit '/pages/about'
    sleep 2
    visit '/pages/blog'
    sleep 2
    visit '/pages/contact'
    sleep 2
    visit '/pages/compare'
    sleep 2
    visit '/pages/whatif'
    sleep 2
    visit '/csv/reg4.csv'
    sleep 2
    visit 'https://github.com/danbikle/reg4us'
    sleep 2
    # I should see Chrome; then it should exit.
  end
end



