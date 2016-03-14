# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Index, Integer, String, Table, text, create_engine
from sqlalchemy.dialects.mysql.base import YEAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
metadata = Base.metadata


class TbAuth(Base):
    __tablename__ = 'tb_auth'

    permission = Column(Integer, primary_key=True)


class TbAuthentication(Base):
    __tablename__ = 'tb_authentication'

    id = Column(Integer, primary_key=True)
    enterprise_id = Column(Integer, nullable=False)
    code = Column(String(128), nullable=False)
    url1 = Column(String(128), nullable=False)
    url2 = Column(String(128))


class TbCity(Base):
    __tablename__ = 'tb_city'

    name = Column(String(64), primary_key=True)
    code = Column(String(64), nullable=False)
    province = Column(String(64), nullable=False, index=True)


class TbEducation(Base):
    __tablename__ = 'tb_education'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey(u'tb_student.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    university = Column(ForeignKey(u'tb_university.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    degree = Column(String(24), nullable=False)
    graduation_year = Column(YEAR(4), nullable=False)
    major = Column(ForeignKey(u'tb_major.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)

    tb_major = relationship(u'TbMajor')
    student = relationship(u'TbStudent')
    tb_university = relationship(u'TbUniversity')


class TbEnterprise(Base):
    __tablename__ = 'tb_enterprise'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, index=True)
    short_name = Column(String(64))
    scale = Column(String(128))
    nature = Column(String(64))
    province = Column(ForeignKey(u'tb_province.name', onupdate=u'CASCADE'), index=True)
    city = Column(ForeignKey(u'tb_city.name', onupdate=u'CASCADE'), index=True)
    address = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    offical_website = Column(String(128))
    logo = Column(String(128))
    describes = Column(String(1024))
    status = Column(Integer)

    tb_city = relationship(u'TbCity')
    tb_province = relationship(u'TbProvince')


class TbEnterpriseStaff(Base):
    __tablename__ = 'tb_enterprise_staff'

    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey(u'tb_user.uid', onupdate=u'CASCADE'), nullable=False, index=True)
    enterprise_id = Column(Integer)
    name = Column(String(64), nullable=False)
    phone = Column(String(21), nullable=False)
    email = Column(String(128))

    tb_user = relationship(u'TbUser')


class TbInstructor(Base):
    __tablename__ = 'tb_instructor'

    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey(u'tb_user.uid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    name = Column(String(64), nullable=False)
    phone = Column(String(21), nullable=False)
    email = Column(String(128))
    university = Column(ForeignKey(u'tb_university.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    major = Column(ForeignKey(u'tb_major.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)

    tb_major = relationship(u'TbMajor')
    tb_user = relationship(u'TbUser')
    tb_university = relationship(u'TbUniversity')


class TbInterviewNotice(Base):
    __tablename__ = 'tb_interview_notice'

    id = Column(Integer, primary_key=True)
    resume_recruit_id = Column(ForeignKey(u'tb_resume_recruit.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    notice = Column(String(2048), nullable=False)
    time = Column(DateTime)
    place = Column(String(256))
    intent = Column(Integer)
    result = Column(String(128))
    phone = Column(String(32))
    conn_name = Column(String(64))

    resume_recruit = relationship(u'TbResumeRecruit')


class TbInterviewNoticePattern(Base):
    __tablename__ = 'tb_interview_notice_pattern'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    enterprise_id = Column(ForeignKey(u'tb_enterprise.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    content = Column(String(2048))
    time = Column(DateTime)
    place = Column(String(256))
    defaults = Column(Integer, nullable=False)
    conn_name = Column(String(64))
    phone = Column(String(32))

    enterprise = relationship(u'TbEnterprise')


class TbMajor(Base):
    __tablename__ = 'tb_major'

    name = Column(String(128), primary_key=True, index=True)
    index1 = Column(String(128), nullable=False, index=True)
    index2 = Column(String(128), nullable=False, index=True)


class TbOfferNotice(Base):
    __tablename__ = 'tb_offer_notice'

    id = Column(Integer, primary_key=True)
    resume_recruit_id = Column(ForeignKey(u'tb_resume_recruit.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    notice = Column(String(2048), nullable=False)
    conn_name = Column(String(64))
    phone = Column(String(32))
    intent = Column(Integer)
    defaults = Column(Integer, nullable=False)

    resume_recruit = relationship(u'TbResumeRecruit')


class TbOfferNoticePattern(Base):
    __tablename__ = 'tb_offer_notice_pattern'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    enterprise_id = Column(ForeignKey(u'tb_enterprise.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    content = Column(String(2048))
    conn_name = Column(String(64))
    phone = Column(String(32))
    defaults = Column(Integer, nullable=False)

    enterprise = relationship(u'TbEnterprise')


class TbProject(Base):
    __tablename__ = 'tb_project'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey(u'tb_student.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    name = Column(String(64), nullable=False)
    start_time = Column(Date, nullable=False)
    end_time = Column(Date, nullable=False)
    describes = Column(String(1024), nullable=False)

    student = relationship(u'TbStudent')


class TbProvince(Base):
    __tablename__ = 'tb_province'

    name = Column(String(64), primary_key=True)
    code = Column(String(64), nullable=False)


class TbRecruitMeeting(Base):
    __tablename__ = 'tb_recruit_meeting'

    id = Column(Integer, primary_key=True)
    recruit_notice_id = Column(ForeignKey(u'tb_recruit_notice.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    begin_time = Column(DateTime)
    end_time = Column(DateTime)
    province = Column(String(128))
    city = Column(String(128))
    university = Column(String(128))
    address = Column(String(256))
    major_required = Column(String(1024), nullable=False)
    information = Column(String(2048), nullable=False)
    status = Column(Integer, nullable=False, server_default=text("'1'"))
    post_time = Column(DateTime)
    name = Column(String(64))

    recruit_notice = relationship(u'TbRecruitNotice')


class TbRecruitNotice(Base):
    __tablename__ = 'tb_recruit_notice'
    __table_args__ = (
        Index('ix_begin_end', 'end_time', 'status'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    enterprise_id = Column(ForeignKey(u'tb_enterprise.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    end_time = Column(Date, nullable=False)
    city = Column(String(128), nullable=False)
    type = Column(String(24), nullable=False)
    work_address = Column(String(256))
    major_required = Column(String(1024), nullable=False)
    information = Column(String(2048), nullable=False)
    required_university = Column(Integer, server_default=text("'0'"))
    required_major = Column(Integer, server_default=text("'0'"))
    status = Column(Integer, nullable=False, server_default=text("'1'"))
    temptation = Column(String(512))
    post_time = Column(DateTime, nullable=False)

    enterprise = relationship(u'TbEnterprise')


class TbRequiredMajor(Base):
    __tablename__ = 'tb_required_major'

    id = Column(Integer, primary_key=True)
    recruit_notice_id = Column(ForeignKey(u'tb_recruit_notice.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    major = Column(String(64), nullable=False)

    recruit_notice = relationship(u'TbRecruitNotice')


class TbRequiredUniversity(Base):
    __tablename__ = 'tb_required_university'

    id = Column(Integer, primary_key=True)
    recruit_notice_id = Column(ForeignKey(u'tb_recruit_notice.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    university = Column(String(64), nullable=False)

    recruit_notice = relationship(u'TbRecruitNotice')


class TbResumeRecruit(Base):
    __tablename__ = 'tb_resume_recruit'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey(u'tb_student.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    recruit_notice_id = Column(ForeignKey(u'tb_recruit_notice.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    status = Column(ForeignKey(u'tb_resume_recruit_status.status', onupdate=u'CASCADE'), nullable=False, index=True, server_default=text("'???'"))

    recruit_notice = relationship(u'TbRecruitNotice')
    tb_resume_recruit_statu = relationship(u'TbResumeRecruitStatu')
    student = relationship(u'TbStudent')


class TbResumeRecruitStatu(Base):
    __tablename__ = 'tb_resume_recruit_status'

    status = Column(String(64), primary_key=True)


class TbResumeStatu(Base):
    __tablename__ = 'tb_resume_status'

    id = Column(Integer, primary_key=True)
    resume_recruit_id = Column(Integer, nullable=False)
    status = Column(String(64), nullable=False)
    time = Column(DateTime, nullable=False)


class TbRole(Base):
    __tablename__ = 'tb_role'

    role = Column(String(128), primary_key=True, unique=True)


class TbRoleAuth(Base):
    __tablename__ = 'tb_role_auth'

    id = Column(Integer, primary_key=True)
    role = Column(ForeignKey(u'tb_role.role', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    permission = Column(ForeignKey(u'tb_auth.permission', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)

    tb_auth = relationship(u'TbAuth')
    tb_role = relationship(u'TbRole')


class TbSelfDescribe(Base):
    __tablename__ = 'tb_self_describe'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey(u'tb_student.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    salary_expect = Column(String(24))
    city_except = Column(String(32))
    residence_except = Column(Integer, server_default=text("'0'"))
    self_describe = Column(String(1024))

    student = relationship(u'TbStudent')


class TbStudent(Base):
    __tablename__ = 'tb_student'
    __table_args__ = (
        Index('ix_university_major', 'university', 'major'),
    )

    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey(u'tb_user.uid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    phone = Column(String(11), nullable=False)
    email = Column(String(128), nullable=False)
    name = Column(String(32), nullable=False)
    gender = Column(String(8), nullable=False)
    birth = Column(Date, nullable=False)
    home_province = Column(ForeignKey(u'tb_province.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), index=True)
    home_city = Column(ForeignKey(u'tb_city.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), index=True)
    address = Column(String(128))
    now_city = Column(ForeignKey(u'tb_city.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), index=True)
    university = Column(ForeignKey(u'tb_university.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    major = Column(ForeignKey(u'tb_major.name', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    student_no = Column(String(32))
    class_name = Column(String(128))
    graduation_year = Column(YEAR(4), nullable=False)
    degree = Column(String(24), nullable=False)
    school_len = Column(Float, nullable=False)
    picture_url = Column(String(128))
    resume_url = Column(String(128))
    political_status = Column(String(24))
    authentication = Column(Integer, nullable=False, server_default=text("'0'"))
    status = Column(Integer)

    tb_city = relationship(u'TbCity', primaryjoin='TbStudent.home_city == TbCity.name')
    tb_province = relationship(u'TbProvince')
    tb_major = relationship(u'TbMajor')
    tb_city1 = relationship(u'TbCity', primaryjoin='TbStudent.now_city == TbCity.name')
    tb_user = relationship(u'TbUser')
    tb_university = relationship(u'TbUniversity')


class TbFormContainer(TbStudent):
    __tablename__ = 'tb_form_container'

    student_id = Column(ForeignKey(u'tb_student.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), primary_key=True)
    bool1 = Column(Integer)
    bool2 = Column(Integer)
    bool3 = Column(Integer)
    bool4 = Column(Integer)
    bool5 = Column(Integer)
    bool6 = Column(Integer)
    bool7 = Column(Integer)
    bool8 = Column(Integer)
    bool9 = Column(Integer)
    bool10 = Column(Integer)
    bool11 = Column(Integer)
    bool12 = Column(Integer)
    bool13 = Column(Integer)
    bool14 = Column(Integer)
    bool15 = Column(Integer)
    bool16 = Column(Integer)
    bool17 = Column(Integer)
    bool18 = Column(Integer)
    bool19 = Column(Integer)
    bool20 = Column(Integer)
    str1 = Column(String(512))
    str2 = Column(String(512))
    str3 = Column(String(512))
    str4 = Column(String(512))
    str5 = Column(String(512))
    str6 = Column(String(512))
    str7 = Column(String(512))
    str8 = Column(String(512))
    str9 = Column(String(512))
    str10 = Column(String(512))
    str11 = Column(String(512))
    str12 = Column(String(512))
    str13 = Column(String(512))
    str14 = Column(String(512))
    str15 = Column(String(512))
    str16 = Column(String(512))
    str17 = Column(String(512))
    str18 = Column(String(512))
    str19 = Column(String(512))
    str20 = Column(String(512))
    time1 = Column(Date)
    time2 = Column(Date)
    time3 = Column(Date)
    time4 = Column(Date)
    time5 = Column(Date)
    time6 = Column(Date)
    time7 = Column(Date)
    time8 = Column(Date)
    time9 = Column(Date)
    time10 = Column(Date)
    form_name = Column(String(256), nullable=False)


class TbUniversity(Base):
    __tablename__ = 'tb_university'

    name = Column(String(128), primary_key=True)
    province = Column(ForeignKey(u'tb_province.name', onupdate=u'CASCADE'), nullable=False, index=True)
    city = Column(ForeignKey(u'tb_city.name', onupdate=u'CASCADE'), nullable=False, index=True)
    address = Column(String(256))
    type = Column(String(64))
    describes = Column(String(2048))

    tb_city = relationship(u'TbCity')
    tb_province = relationship(u'TbProvince')


class TbUniversityForm(Base):
    __tablename__ = 'tb_university_form'

    id = Column(Integer, primary_key=True)
    column_name = Column(String(36), nullable=False)
    title = Column(String(256), nullable=False)
    university = Column(String(128), nullable=False)
    type = Column(String(64), nullable=False)
    form_name = Column(String(256), nullable=False)


class TbUser(Base):
    __tablename__ = 'tb_user'
    __table_args__ = (
        Index('ix_phone_password', 'phone', 'password'),
    )

    uid = Column(String(64), primary_key=True)
    phone = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False)
    token = Column(String(64))
    complete = Column(Integer, nullable=False, server_default=text("'1'"))
    created = Column(DateTime)
    last_login = Column(DateTime)
    login_count = Column(Integer)
    phone_check = Column(Integer, nullable=False, server_default=text("'0'"))
    email_check = Column(Integer, nullable=False, server_default=text("'0'"))


class TbUserRole(Base):
    __tablename__ = 'tb_user_role'

    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey(u'tb_user.uid', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    role = Column(ForeignKey(u'tb_role.role', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    auth = Column(Integer, nullable=False)

    tb_role = relationship(u'TbRole')
    tb_user = relationship(u'TbUser')


class TbWorkExperience(Base):
    __tablename__ = 'tb_work_experience'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey(u'tb_student.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    name = Column(String(64))
    start_time = Column(Date, nullable=False)
    end_time = Column(Date, nullable=False)
    type = Column(String(24))
    work_content = Column(String(1024), nullable=False)
    position = Column(String(32), nullable=False)

    student = relationship(u'TbStudent')


class TbWrittenExamNotice(Base):
    __tablename__ = 'tb_written_exam_notice'

    id = Column(Integer, primary_key=True)
    resume_recruit_id = Column(ForeignKey(u'tb_resume_recruit.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    notice = Column(String(2048), nullable=False)
    time = Column(DateTime)
    place = Column(String(256))
    intent = Column(Integer)
    result = Column(String(128))
    conn_name = Column(String(64))
    phone = Column(String(32))

    resume_recruit = relationship(u'TbResumeRecruit')


class TbWrittenExamNoticePattern(Base):
    __tablename__ = 'tb_written_exam_notice_pattern'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    enterprise_id = Column(ForeignKey(u'tb_enterprise.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False, index=True)
    content = Column(String(2048))
    time = Column(DateTime)
    place = Column(String(256))
    defaults = Column(Integer, nullable=False)
    phone = Column(String(32))
    conn_name = Column(String(64))

    enterprise = relationship(u'TbEnterprise')


t_test = Table(
    'test', metadata,
    Column('uid', String(64)),
    Column('password', String(64)),
    Column('phone', String(32))
)

# 初始化数据库连接:
engine = create_engine('mysql://root:1990221@localhost:3306/recruit')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
