// Camera Testing

import Camera from '@/components/Camera.vue'
import { mount } from '@vue/test-utils'

describe('Click event', () => {
  it('Click on update button calls our method getTemp', () => {
    const wrapper = mount(Camera)
    wrapper.find('button').trigger('click')
  })
  it('testing chossenVideo', () => {

  })
})
