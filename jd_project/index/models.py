from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class ShAd(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ad_name = models.CharField(max_length=45)
    pos_id = models.IntegerField()
    is_on = models.CharField(max_length=1)
    ad_type = models.CharField(max_length=2)
    img_url = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_ad'


class ShAdInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    img_url = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    # ad_id = models.IntegerField()
    shad = models.OneToOneField(ShAd)

    class Meta:
        managed = False
        db_table = 'sh_ad_info'


class ShAdPos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pos_name = models.CharField(max_length=45)
    pos_width = models.IntegerField()
    pos_height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_ad_pos'


class ShAdmin(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=32)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_admin'


class ShArticle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=45)
    content = models.TextField()
    cat_id = models.IntegerField()
    addtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sh_article'


class ShArticleCat(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cat_name = models.CharField(max_length=45)
    is_help = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sh_article_cat'


class ShAttribute(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    attr_name = models.CharField(max_length=30)
    attr_type = models.CharField(max_length=2)
    attr_values = models.CharField(max_length=300)
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_attribute'


class ShBrand(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    brand_name = models.CharField(max_length=30)
    brand_logo = models.CharField(max_length=150)
    brand_url = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_brand'


class ShButtons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    btn_name = models.CharField(max_length=30)
    btn_url = models.CharField(max_length=150)
    open_new = models.CharField(max_length=1)
    btn_pos = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sh_buttons'


class ShCategory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cat_name = models.CharField(max_length=30)
    parent_id = models.IntegerField()
    filter_goods_attr_id = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_category'


class ShGoods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    goods_name = models.CharField(max_length=30)
    sn = models.CharField(max_length=16)
    logo = models.CharField(max_length=150)
    sm_logo = models.CharField(max_length=150)
    mid_logo = models.CharField(max_length=150)
    big_logo = models.CharField(max_length=150)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_on_sale = models.CharField(max_length=1)
    cat_id = models.IntegerField()
    brand_id = models.IntegerField()
    type_id = models.IntegerField()
    goods_desc = models.TextField(blank=True)
    goods_weight = models.DecimalField(max_digits=10, decimal_places=2)
    weight_unit = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sh_goods'


class ShGoodsAttr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    goods_id = models.IntegerField()
    attr_id = models.IntegerField()
    attr_value = models.CharField(max_length=150)
    attr_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sh_goods_attr'


class ShGoodsPic(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    goods_id = models.IntegerField()
    logo = models.CharField(max_length=150)
    sm_logo = models.CharField(max_length=150)
    big_logo = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_goods_pic'


class ShMember(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    face = models.CharField(max_length=150)
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=32)
    addtime = models.DateTimeField()
    gender = models.CharField(max_length=2)
    email_checked = models.CharField(max_length=3)
    email_chk_str = models.CharField(max_length=32)
    get_pass_code = models.CharField(max_length=7)
    get_pass_code_time = models.IntegerField()
    jifen = models.IntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sh_member'


class ShMemberAddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    shr_name = models.CharField(max_length=30)
    shr_province = models.CharField(max_length=30)
    shr_city = models.CharField(max_length=30)
    shr_area = models.CharField(max_length=30)
    shr_address = models.CharField(max_length=30)
    shr_phone = models.CharField(max_length=30)
    member_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_member_address'


class ShMemberLevel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    level_name = models.CharField(max_length=30)
    num_bottom = models.IntegerField()
    num_top = models.IntegerField()
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_member_level'


class ShMemberPrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level_id = models.IntegerField()
    goods_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_member_price'


class ShOrder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sn = models.CharField(max_length=16)
    addtime = models.DateTimeField()
    shr_name = models.CharField(max_length=30)
    shr_province = models.CharField(max_length=30)
    shr_city = models.CharField(max_length=30)
    shr_area = models.CharField(max_length=30)
    shr_address = models.CharField(max_length=30)
    shr_phone = models.CharField(max_length=30)
    member_id = models.IntegerField()
    delivery = models.CharField(max_length=30)
    pay = models.CharField(max_length=30)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_tprice = models.DecimalField(max_digits=10, decimal_places=2)
    yunfei = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.IntegerField()
    pay_status = models.IntegerField()
    delivery_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_order'


class ShOrderGoods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    order_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_attr_id = models.CharField(max_length=150)
    goods_attr_str = models.CharField(max_length=150)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_number = models.IntegerField()
    goods_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_order_goods'


class ShPrivilege(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pri_name = models.CharField(max_length=30)
    module_name = models.CharField(max_length=30)
    controller_name = models.CharField(max_length=30)
    action_name = models.CharField(max_length=30)
    parent_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_privilege'


class ShProduct(models.Model):
    goods_id = models.IntegerField()
    goods_number = models.IntegerField()
    goods_attr = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_product'


class ShRecommend(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    rec_name = models.CharField(max_length=30)
    rec_type = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sh_recommend'


class ShRecommendItem(models.Model):
    rec_id = models.IntegerField()
    value_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_recommend_item'


class ShRemark(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    star = models.IntegerField()
    content = models.CharField(max_length=600)
    goods_id = models.IntegerField()
    addtime = models.DateTimeField()
    member_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_remark'


class ShRole(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    role_name = models.CharField(max_length=30)
    pri_id_list = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'sh_role'


class ShShopConfig(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    config_name = models.CharField(max_length=150)
    config_type = models.CharField(max_length=4)
    config_values = models.CharField(max_length=600)
    config_value = models.CharField(max_length=600)

    class Meta:
        managed = False
        db_table = 'sh_shop_config'


class ShType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sh_type'


class ShYinxiang(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    yx_name = models.CharField(max_length=30)
    yx_count = models.IntegerField()
    goods_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_yinxiang'
